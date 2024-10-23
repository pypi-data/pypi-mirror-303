import sqlite3
import datetime
import logging
logging.basicConfig(level=logging.INFO)

class Field:
    def __init__(self, primary_key=False, unique=False, null=True, default=None):
        self.primary_key = primary_key
        self.unique = unique
        self.null = null
        self.default = default

    def validate(self, value):
        if not self.null and value is None:
            raise ValueError("This field cannot be null.")
        return value

class IntegerField(Field):
    """
    Represents an integer field in a model.
    params:
    - primary_key
    - unique
    - null
    - default
    """
    def validate(self, value):
        value = super().validate(value)
        if value is not None and not isinstance(value, int):
            raise ValueError("IntegerField must be an integer.")
        return value

class CharField(Field):
    """
    Represents a character field in a model.
    params:
    - primary_key
    - unique
    - null
    - default
    - max_length (default: 255)
    """
    def __init__(self, max_length=255, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        value = super().validate(value)
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("CharField must be a string.")
            if len(value) > self.max_length:
                raise ValueError(f"CharField must not exceed {self.max_length} characters.")
        return value

class TextField(Field):
    """
    Represents a text field in a model.
    params:
    - primary_key
    - unique
    - null
    - default
    - max_length (default: 500)
    """
    def __init__(self, max_length=500, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        value = super().validate(value)
        if value is not None and not isinstance(value, str):
            raise ValueError("TextField must be a string.")
        return value

class BooleanField(Field):
    """
    Represents a boolean field in a model.
    params:
    - primary_key
    - unique
    - null
    - default
    """
    def validate(self, value):
        value = super().validate(value)
        if value is not None and not isinstance(value, bool):
            raise ValueError("BooleanField must be a boolean.")
        return value

class DateTimeField(Field):
    """
    Represents a datetime field in a model.
    params:
    - primary_key
    - unique
    - null
    - default
    """
    def validate(self, value):
        value = super().validate(value)
        if value is not None:
            if not isinstance(value, (datetime.datetime, str)):
                raise ValueError("DateTimeField must be a datetime object or an ISO formatted string.")
            if isinstance(value, str):
                try:
                    datetime.datetime.fromisoformat(value)
                except ValueError:
                    raise ValueError("DateTimeField string must be in ISO format.")
        return value



class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                new_class._meta[key] = value
        return new_class

class Model:
    _db_name = 'darkgram.db'

    def __init__(self, **kwargs):
        for name, field in self.__class__._meta.items():
            setattr(self, name, kwargs.get(name, field.default))


    @classmethod
    def set_db_name(cls, name):
        """
        Set the database name for the model.
        params:
        - name (str): The new database name for the model.
        """
        cls._db_name = name

    @classmethod
    def create_table(cls):
        """
        Create the table for the model in the database.
        """
        conn = sqlite3.connect(cls._db_name)
        cursor = conn.cursor()
        fields = []
        for name, field in cls._meta.items():
            field_type = "INTEGER" if isinstance(field, IntegerField) else "TEXT"
            null_str = "NOT NULL" if not field.null else ""
            unique_str = "UNIQUE" if field.unique else ""
            primary_key_str = "PRIMARY KEY" if field.primary_key else ""
            fields.append(f"{name} {field_type} {null_str} {unique_str} {primary_key_str}")
        query = f"CREATE TABLE IF NOT EXISTS {cls.__name__} ({', '.join(fields)})"
        cursor.execute(query)
        conn.commit()
        conn.close()

    def save(self):
        """
        Save the model to the database.
        """
        conn = sqlite3.connect(self._db_name)
        cursor = conn.cursor()
        fields = []
        values = []
        placeholders = []
        for name, field in self.__class__._meta.items():
            if name != 'id' or getattr(self, 'id') is not None:
                fields.append(name)
                value = getattr(self, name)
                logging.debug(f"Field: {name}, Value: {value}, Type: {type(value)}")

                if isinstance(field, DateTimeField) and isinstance(value, datetime.datetime):
                    value = value.isoformat()
                elif isinstance(field, BooleanField):
                    value = 1 if value else 0

                values.append(value)
                placeholders.append('?')

        if getattr(self, 'id') is None:
            query = f"INSERT INTO {self.__class__.__name__} ({', '.join(fields)}) VALUES ({', '.join(placeholders)})"
        else:
            set_clause = ', '.join([f"{field} = ?" for field in fields])
            query = f"UPDATE {self.__class__.__name__} SET {set_clause} WHERE id = ?"
            values.append(getattr(self, 'id'))

        logging.debug(f"Query: {query}")
        logging.debug(f"Values: {values}")

        try:
            cursor.execute(query, values)
            if getattr(self, 'id') is None:
                self.id = cursor.lastrowid
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"SQLite error: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def _get_field_type(field):
        if isinstance(field, IntegerField):
            return "INTEGER"
        elif isinstance(field, CharField):
            return f"VARCHAR({field.max_length})"
        elif isinstance(field, TextField):
            return "TEXT"
        elif isinstance(field, BooleanField):
            return "BOOLEAN"
        elif isinstance(field, DateTimeField):
            return "DATETIME"
        else:
            raise ValueError(f"Unsupported field type: {type(field)}")

    @classmethod
    def get(cls, **kwargs):
        """
        Retrieve a single model instance from the database based on the provided kwargs.
        params:
        - kwargs (dict): A dictionary of field names and their corresponding values.
        Returns:
        - An instance of the model if a matching record is found, or None otherwise.
        """
        conn = sqlite3.connect(cls._db_name)
        cursor = conn.cursor()
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query = f"SELECT * FROM {cls.__name__} WHERE {' AND '.join(conditions)}"
        cursor.execute(query, values)
        row = cursor.fetchone()
        conn.close()
        if row:
            instance = cls()
            for i, (name, field) in enumerate(cls._meta.items()):
                value = row[i]
                if isinstance(field, DateTimeField) and value is not None:
                    value = datetime.datetime.fromisoformat(value)
                elif isinstance(field, BooleanField):
                    value = bool(value)
                setattr(instance, name, value)
            return instance
        return None

    @classmethod
    def filter(cls, **kwargs):
        """
        Retrieve a list of model instances from the database based on the provided kwargs.
        params:
        - kwargs (dict): A dictionary of field names and their corresponding values.
        Returns:
        - A list of instances of the model if matching records are found, or an empty list otherwise.
        """
        conn = sqlite3.connect(cls._db_name)
        cursor = conn.cursor()
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query = f"SELECT * FROM {cls.__name__}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        cursor.execute(query, values)
        rows = cursor.fetchall()
        conn.close()

        instances = []
        for row in rows:
            instance = cls()
            for i, name in enumerate(cls._meta.keys()):
                setattr(instance, name, row[i])
            instances.append(instance)
        return instances

    @classmethod
    def all(cls):
        """
        Retrieve all model instances from the database.
        Returns:
        - A list of instances of the model.
        """
        conn = sqlite3.connect(cls._db_name)
        cursor = conn.cursor()
        query = f"SELECT * FROM {cls.__name__}"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        instances = []
        for row in rows:
            instance = cls()
            for i, name in enumerate(cls._meta.keys()):
                setattr(instance, name, row[i])
            instances.append(instance)
        return instances

    @classmethod
    def delete(cls, **kwargs):
        """
        Delete model instances from the database based on the provided kwargs.
        params:
        - kwargs (dict): A dictionary of field names and their corresponding values.
        Returns:
        - The number of rows deleted.
        """
        conn = sqlite3.connect(cls._db_name)
        cursor = conn.cursor()
        conditions = []
        values = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values.append(value)
        query = f"DELETE FROM {cls.__name__}"
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return cursor.rowcount

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join([f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_')])})"

    def __repr__(self):
        return self.__str__()
