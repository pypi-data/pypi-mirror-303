import psycopg2
from typing import List

from pyway.migration import Migration
from pyway.configfile import ConfigFile


CREATE_VERSION_MIGRATIONS = "create table if not exists %s ("\
    "installed_rank serial PRIMARY KEY,"\
    "version varchar(20) NOT NULL,"\
    "extension varchar(20) NOT NULL,"\
    "name varchar(125) NOT NULL,"\
    "checksum varchar(25) NOT NULL,"\
    "apply_timestamp timestamp DEFAULT NOW()"\
    ");"
SELECT_FIELDS = ("version", "extension", "name", "checksum", "apply_timestamp")
ORDER_BY_FIELD_ASC = "installed_rank"
ORDER_BY_FIELD_DESC = "installed_rank desc"
INSERT_VERSION_MIGRATE = "insert into %s (version, extension, name, checksum) values ('%s', '%s', '%s', '%s');"
UPDATE_CHECKSUM = "update %s set checksum='%s' where version='%s';"


class Postgres():

    def __init__(self, args: ConfigFile) -> None:
        self.args = args
        self.version_table = args.database_table
        self.create_version_table_if_not_exists()

    def connect(self) -> psycopg2.extensions.connection:
        connection_string = f"dbname={self.args.database_name} user={self.args.database_username}"
        connection_string += f" host={self.args.database_host}"

        if self.args.database_password:
            connection_string += f" password={self.args.database_password}"

        if self.args.database_port:
            connection_string += f" port={self.args.database_port}"

        return psycopg2.connect(connection_string)

    def create_version_table_if_not_exists(self) -> None:
        self.execute(CREATE_VERSION_MIGRATIONS % self.version_table)

    def execute(self, script: str) -> None:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(script)
        conn.commit()

    def get_all_schema_migrations(self) -> List[Migration]:
        cnx = self.connect()
        cursor = cnx.cursor()
        cursor.execute(f"SELECT {','.join(SELECT_FIELDS)} FROM {self.version_table} ORDER BY {ORDER_BY_FIELD_ASC}")
        migrations = []
        for row in cursor.fetchall():
            migrations.append(Migration(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        cnx.close()
        return migrations

    def get_schema_migration(self, version: str) -> Migration:
        cnx = self.connect()
        cursor = cnx.cursor()
        cursor.execute(f"SELECT {','.join(SELECT_FIELDS)} FROM {self.version_table} WHERE version=%s", [version])
        row = cursor.fetchone()
        if row is not None:
            migration = Migration(row[0], row[1], row[2], row[3], row[4])
        cursor.close()
        cnx.close()
        return migration

    def upgrade_version(self, migration: Migration) -> None:
        self.execute(INSERT_VERSION_MIGRATE % (self.version_table, migration.version,
                                               migration.extension, migration.name,
                                               migration.checksum))

    def update_checksum(self, migration: Migration) -> None:
        self.execute(UPDATE_CHECKSUM % (self.version_table, migration.checksum, migration.version))
