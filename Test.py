    def create_database(self, database_name):
        query = "create database %s;" % (database_name)
        print(query)
        self._db_client.execute(query)


    def show_databases(self):
        query = "show databases;"
        print(query)
        self._db_client.execute(query)
        databases = self._db_client.fetchall()
        for database in databases:
            print(database)


    def use_database(self, database_name):
        query = "use %s;" % (database_name)
        print(query)
        self._db_client.execute(query)


    def show_tables(self):
        query = "show tables;"
        print(query)
        self._db_client.execute(query)
        databases = self._db_client.fetchall()
        for database in databases:
            print(database)


    columns = "col_name, datatype, constraint"


    def create_table(self, database_name, table_name, db_type, columns):
        if db_type.upper() == "MYSQL":
            create_database(database_name)
            show_databases()
            use_database(database_name)
            query = "create table %s (%s);" % (table_name, columns)
            print(query)
            self._db_client.execute(query)
            show_tables()
            self._db_client.connection.commit()


    def insert_into(self, config, table_name, db_type, fields=None, values=None):
        result = None

        if db_type.upper() == "MSSQL":
            self._connect_to_mssqlDB(config)
            query = "insert into %s (%s) values (%s);" % (table_name, fields, values)
            self._db_client.execute(query)
            self._db_client.connection.commit()
        if db_type.upper() == "MONGODB":
            self._connect_to_mongoDB(config)
            result = self.database.get_collection(table_name).insert(values)
            return result
        if db_type.upper() == "ORIENTDB":
            self._connect_to_orientDB(config)
            query = "insert into %s (%s) values (%s);" % (table_name, fields, values)
            self._db_client.command(query)
        if db_type.upper() == "ORACLE":
            self._connect_to_OracleDB(config)
            query = "insert into %s (%s) values (%s)" % (table_name, fields, values)
            self._db_client.execute(query)
            self._db_client.connection.commit()
        if db_type.upper() == "MYSQL":
            self._connect_to_mysqlDB(config)
            query = "insert into %s (%s) values (%s);" % (table_name, fields, values)
            print(query)
            self._db_client.execute(query)
            self._db_client.connection.commit()


    def update_inserted_record(self, config, table_name, db_type, to_update_value, current_value):
        if db_type.upper() == "MYSQL":
            self._connect_to_mysqlDB(config)
            query = "UPDATE %s SET %s WHERE %s;" % (table_name, to_update_value, current_value)
            print(query)
            self._db_client.execute(query)
            self._db_client.connection.commit()


    def delete_inserted_record(self, config, table_name, db_type, fields=None):
        if db_type.upper() == "MONGODB":
            self._connect_to_mongoDB(config)
            result = self.database.get_collection(table_name).delete_many(fields)
            return result
        if db_type.upper() == "MSSQL":
            self._connect_to_mssqlDB(config)
            query = "DELETE from %s WHERE (%s);" % (table_name, fields)
            print(query)
            self._db_client.execute(query)

            self._db_client.connection.commit()
        if db_type.upper() == "ORIENTDB":
            self._connect_to_orientDB(config)
            query = "DELETE from %s WHERE (%s);" % (table_name, fields)
            self._db_client.command(query)
        if db_type.upper() == "MYSQL":
            self._connect_to_mysqlDB(config)
            query = "DELETE from %s WHERE %s;" % (table_name, fields)
            print(query)
            self._db_client.execute(query)
            self._db_client.connection.commit()


    def drop_table(self, table_name):
        query = "DROP TABLE %s;" % (table_name)
        print(query)
        self._db_client.execute(query)


    def drop_database(self, config, table_name, database_name, db_type):
        if db_type.upper() == "MYSQL":
            self._connect_to_mysqlDB(config)
            drop_table(table_name)
            query = "DROP DATABASE %s;" % (database_name)
            print(query)
            self._db_client.execute(query)
            self._db_client.connection.commit()