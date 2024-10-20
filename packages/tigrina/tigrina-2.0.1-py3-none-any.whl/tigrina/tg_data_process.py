import pandas as pd
import re
import os
import pkg_resources

version="production"
currentDir = os.path.dirname(os.path.abspath(__file__))
if version == "test":
    global_container_folder = os.path.join(currentDir, "tg_data")
else:
    global_container_folder = pkg_resources.resource_filename(__name__, 'tg_data')

def lowercase_sql_keywords(sql_query):
    keywords = [
        "INSERT INTO", "SELECT", "FROM", "INNER JOIN", "OUTER JOIN", "LEFT JOIN",
        "RIGHT JOIN", "NATURAL JOIN", "WHERE", "LIKE", "IN", "ORDER BY", 
        "GROUP BY", "UPDATE", "SET"
    ]

    # Use regex to replace only whole words, case-insensitively
    for keyword in keywords:
        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
        sql_query = pattern.sub(keyword.lower(), sql_query)

    return sql_query

def get_table_fields(query):
    table_name = query.split(' ')[1]
    path = os.path.join(global_container_folder, f"{table_name}.csv")
    if os.path.exists(path):
        df = pd.read_csv(path, nrows=0)  # Read only the header row
        header_collection = list(df.columns)
        return header_collection
    else:
        return "Table not found."

def get_tables(query):
    if query == "show tables":
        dir_path = global_container_folder
        filenames = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.csv'):
                    filenames.append(file.split('.')[0])

        list_of_tables = filenames
        return filenames
    else:
        return "wrong show tables query syntax."
    
def extract_table_name(sql_query):
    try:
        # Normalize the query to lowercase to make regex case-insensitive
        normalized_query = sql_query.lower()
        
        # Regular expressions for different types of queries
        insert_regex = re.compile(r"insert\s+into\s+(\w+)")
        select_regex = re.compile(r"from\s+(\w+)")
        delete_regex = re.compile(r"delete\s+from\s+(\w+)")
        update_regex = re.compile(r"update\s+(\w+)")
        
        table_name = None
        
        if insert_regex.search(normalized_query):
            table_name = insert_regex.search(normalized_query).group(1)
        elif select_regex.search(normalized_query):
            table_name = select_regex.search(normalized_query).group(1)
        elif delete_regex.search(normalized_query):
            table_name = delete_regex.search(normalized_query).group(1)
        elif update_regex.search(normalized_query):
            table_name = update_regex.search(normalized_query).group(1)
        
        if table_name and table_name.endswith('.csv'):
            table_name = table_name.split('.')[0]
        
        return os.path.join(global_container_folder, f"{table_name}.csv")
    except Exception as error:
        return f"There is something wrong: {error}"
def parse_sql_query(query):
    # Remove extra spaces
    query = ' '.join(query.split())

    # Extract the SELECT part
    select_match = re.search(r'select (.+?) from', query, re.IGNORECASE)
    select_fields = select_match.group(1).split(', ') if select_match else []

    # Extract the FROM part
    from_match = re.search(r'from (\w+)', query, re.IGNORECASE)
    from_table = from_match.group(1) if from_match else ''

    # Extract the JOIN part
    join_pattern = re.compile(r'(inner join|outer join|left join|right join|cross join) .+? on .+?=\w+.\w+', re.IGNORECASE)
    join_match = join_pattern.search(query)
    join_info = [join_match.group(0)] if join_match else []

    # Extract the WHERE part
    where_match = re.search(r'where (.+?)( group by| order by| limit|$)', query, re.IGNORECASE)
    where_conditions = []
    if where_match:
        where_part = where_match.group(1)
        conditions = re.split(r' (and|or) ', where_part, flags=re.IGNORECASE)
        where_conditions = [conditions[i] if i % 2 == 0 else {'connector': conditions[i].lower()} for i in range(len(conditions))]

    # Reconstruct the where_conditions list properly
    final_conditions = []
    i = 0
    while i < len(where_conditions):
        if isinstance(where_conditions[i], dict):
            final_conditions[-1]['connector'] = where_conditions[i]['connector']
        else:
            condition = re.split(r'(=| like | in )', where_conditions[i], flags=re.IGNORECASE)
            key, operator, value = condition[0].strip(), condition[1].strip().lower(), condition[2].strip()
            final_conditions.append({key: f"{operator} {value}"})
        i += 1

    # Extract GROUP BY part
    group_by_match = re.search(r'group by (.+?)( order by| limit|$)', query, re.IGNORECASE)
    group_by = group_by_match.group(1).strip().split(', ') if group_by_match else []

    # Extract ORDER BY part
    order_by_match = re.search(r'order by (.+?)( limit|$)', query, re.IGNORECASE)
    order_by = []
    if order_by_match:
        order_by_part = order_by_match.group(1).strip()
        order_by_clauses = order_by_part.split(', ')
        for clause in order_by_clauses:
            parts = clause.split()
            if len(parts) == 2 and parts[1].lower() in ['asc', 'desc']:
                order_by.append({'field': parts[0], 'order': parts[1].lower()})
            else:
                order_by.append({'field': parts[0], 'order': 'asc'})

    # Extract LIMIT part
    limit_match = re.search(r'limit (\d+)( offset (\d+))?', query, re.IGNORECASE)
    limit_info = {}
    if limit_match:
        limit_info['limit'] = int(limit_match.group(1))
        if limit_match.group(3):
            limit_info['offset'] = int(limit_match.group(3))

    return {
        'select_fields': select_fields,
        'from_table': from_table,
        'join_info': join_info,
        'where_conditions': final_conditions,
        'group_by': group_by,
        'order_by': order_by,
        'limit_info': limit_info
    }

# Example usage

def check_percentage_position(mylike):
    try:
        result=""
        my_string = mylike
        starts_with_percent = my_string.startswith('%') or my_string.startswith('\'%') or my_string.startswith('\"%')
        ends_with_percent = my_string.endswith('%') or my_string.endswith('%\'') or my_string.endswith('%\"') 
        both_start_end = starts_with_percent and ends_with_percent
        
        if starts_with_percent:
            result="front"

        if ends_with_percent:
            result="back"

        if both_start_end:
            result="both"

        if not starts_with_percent and not ends_with_percent:
            result="none"

        return result
    except Exception as error:
        return f"There is something wrong: {error}"

def check_input_fields_in_table(input_fields,table):
    source_fields=get_table_fields(f"describe {table}")
    missing_fields = [field for field in input_fields if field not in source_fields]
    if len(missing_fields) > 0:
        return f"Fields: {''.join(missing_fields)} not found"
    else:
        return []
def select_data(sql_query):
    sql_query = lowercase_sql_keywords(sql_query)
    try:
        parsed_query = parse_sql_query(sql_query)
        select_fields = parsed_query['select_fields']
        print("select_fields:",select_fields)
        from_table=parsed_query['from_table']
        
        if select_fields[0]=='*':
            get_all_fields=get_table_fields(f"describe {from_table}")
            select_fields=get_all_fields
        table_name=extract_table_name(sql_query)
        check_fields=check_input_fields_in_table(select_fields,from_table)
        if len(check_fields) != 0:
            return check_fields
        join_info = parsed_query['join_info']
        where_conditions = parsed_query['where_conditions']
        limit = parsed_query['limit_info']
        order_by = parsed_query['order_by']
        group_by = parsed_query['group_by']
        if len(select_fields) > 0:
            try:
                if len(where_conditions) > 0 :
                    where_fields = [list(condition.keys())[0] for condition in where_conditions]
                    select_fields=select_fields + where_fields
                data = pd.read_csv(table_name, usecols=select_fields)
            except Exception as error:
                    return f"Table '{os.path.basename(table_name.split('.')[0])}' not found."
        
        query_conditions = []
        whatIsWhereQuery='equals'
        modifiedData=data
        if len(where_conditions) > 0:
            for condition in where_conditions:
                for column, value in condition.items():
                    if column != 'connector':
                        if 'in (' in value or 'in(' in value:
                            query_conditions.append(f"{column} {value}")
                            whatIsWhereQuery='in'
                        elif 'like ' in value:
                            like_value = value.split("like")[1].strip()
                            query_conditions.append(column)
                            query_conditions.append(like_value)
                            whatIsWhereQuery='like'
                        else:
                            whatIsWhereQuery='WithLogic'
                            query_conditions.append(f"{column} {value}")
                    else:
                        query_conditions.append(value)
            if whatIsWhereQuery == 'equals':
                query_string = ' '.join(query_conditions).replace('=','==')
                try:
                    modifiedData = data.query(query_string)
                except Exception as error:
                        return f"There is something wrong! {error}"
            elif whatIsWhereQuery == 'WithLogic':
                query_string = ' '.join(query_conditions).replace('=','==')
                try:
                    modifiedData = data.query(query_string)
                except Exception as error:
                        return f"There is something wrong! {error}"
            elif whatIsWhereQuery == 'in':
                query_conditions_modified = []
                for condition in query_conditions:
                    if ' in ' in condition:
                        left_part, right_part = condition.split(' in ')
                        right_part = right_part.strip().strip('()')
                        values = right_part.split(',')
                        converted_values = [convert_to_number_or_keep_string(val.strip().strip("'").strip('"')) for val in values]
                        new_right_part = f"[{', '.join(map(str, converted_values))}]"
                        query_conditions_modified.append(f"{left_part.strip()}.isin({new_right_part})")
                    else:
                        parts = condition.split()
                        if len(parts) == 3:
                            left_part, operator, right_part = parts
                            right_part = convert_to_number_or_keep_string(right_part.strip().strip("'").strip('"'))
                            query_conditions_modified.append(f"{left_part.strip()} {operator} {right_part}")
                        else:
                            query_conditions_modified.append(condition)
                query_string = ' '.join(query_conditions_modified).replace('=','==')
                try:
                    modifiedData = data.query(query_string)
                except Exception as error:
                    return f"There is something wrong! {error}"
            elif whatIsWhereQuery == 'like':
                whereIsPercentage=check_percentage_position(query_conditions[1])
                like_value = query_conditions[1].replace('%','').replace('\'','').replace('\"','')
                column=query_conditions[0]
                if whereIsPercentage == 'both':
                    try:
                        modifiedData = modifiedData[modifiedData[column].str.startswith(like_value) & modifiedData[column].str.endswith(like_value)]
                    except Exception as error:
                        return f"There is something wrong! {error}"
                elif whereIsPercentage == 'front':
                    try:
                        modifiedData = modifiedData[modifiedData[column].str.endswith(like_value)]
                    except Exception as error:
                        return f"There is something wrong! {error}"
                elif whereIsPercentage == 'back':
                    try:
                        modifiedData = modifiedData[modifiedData[column].str.startswith(like_value)]
                    except Exception as error:
                        return f"There is something wrong! {error}"
                elif whereIsPercentage == 'none':
                    try:
                        modifiedData = modifiedData[modifiedData[column].str.contains(like_value)]
                    except Exception as error:
                        return f"There is something wrong! {error}"
        # limit 
        if len(limit) != 0:
            modifiedData = modifiedData.iloc[:limit['limit']]
        # group by
        if len(group_by) != 0:
            groupTest = modifiedData.groupby(group_by)
            group_result=[]
            for group_name, group_data in groupTest:
                    group_result.append(group_data)
        return modifiedData
    except Exception as error:
        return f"There is something wrong: {error}"
def convert_to_number_or_keep_string(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            # Keep it as a string but with quotes
            return f"'{value}'"

def insert_query(sql_query):
    sql_query = lowercase_sql_keywords(sql_query)
    try:
        fields = [field.strip() for field in re.search(r"\(([^)]+)\)", sql_query).group(1).split(',')]
        values = [value.strip().strip("'") for value in re.search(r"values\(([^)]+)\)", sql_query).group(1).split(',')]
        new_object = {}
        for index, field in enumerate(fields):
            if index < len(values):
                new_object[field] = float(values[index]) if values[index].replace('.', '', 1).isdigit() else values[index]

        obj_collection = [new_object]

        table = extract_table_name(sql_query)
        info = {
            "table_name": table,
            "main_obj_collection": obj_collection
        }

        return info
    except Exception as error:
        return f"Error:There is something wrong: {error}"
def insert(sql_query):
    try:
        query_result = insert_query(sql_query)
        objects_list = query_result['main_obj_collection']
        
        fields = list(objects_list[0].keys())
        
        table_name = query_result['table_name']
        check_fields=check_input_fields_in_table(fields,os.path.basename(table_name.split('.')[0]))
        if len(check_fields) != 0:
            return check_fields
        df = pd.DataFrame(objects_list)
        # Check if the file exists
        file_exists = os.path.exists(table_name)
        
        if file_exists:
            existing_df = pd.read_csv(table_name)
            df = df.reindex(columns=existing_df.columns)
        else:
            # If the table (file) is not found, return a specific error message
            if 'fields' in query_result:
                df = df[query_result['fields']]
            else:
                return f"Table '{os.path.basename(table_name.split('.')[0])}' not found."
        
        # Append the data to the file
        df.to_csv(table_name, mode='a', index=False, header=not file_exists)
        return "Inserted successfully."
    
    except FileNotFoundError:
        return f"File '{table_name}' not found."
    except Exception as error:
        return f"Error: There is something wrong: {error}"

insert_query_info = "insert into tb1 (id, name, age, city) values(13,'gide segidrt', 48, 'Nijmegen')"
# insert(insert_query_info)

def update(sql_query):
    query_result = update_query(sql_query)
    if 'Error:' in query_result:
        return f"Probably wrong syntax, check if there is where in the sql query."
    else:
        objects_list = query_result['main_obj_collection']
        table_name = query_result['table_name']
        where_field = query_result['where_field']
        where_value = query_result['where_field_value']

        # Extract the fields to be updated
        fields = list(objects_list[0].keys())
        # print("fields:", fields)

        # Check if the input fields exist in the table
        check_fields = check_input_fields_in_table(fields, os.path.basename(table_name.split('.')[0]))
        if len(check_fields) != 0:
            return check_fields

        try:
            df = pd.read_csv(table_name)
        except FileNotFoundError:
            return f"Table '{os.path.basename(table_name.split('.')[0])}' not found."

        try:
            # Check if the where field exists in the DataFrame
            if where_field not in df.columns:
                return f"Field '{where_field}' not found in the table."

            # Filter the DataFrame to find the matching rows based on the where field and value
            matching_rows = df[df[where_field] == where_value]

            if matching_rows.empty:
                return "Record not found."

            # Update all the specified fields for the matching rows
            for field in fields:
                df.loc[df[where_field] == where_value, field] = objects_list[0][field]

            # Write the updated DataFrame back to the CSV file
            df.to_csv(table_name, index=False)
            return "Updated successfully."

        except Exception as error:
            return f"There is something wrong: {error}"

def update_query(sql_query):
    sql_query = lowercase_sql_keywords(sql_query)
    try:
        # Extract the SET clause and key-value pairs
        try:
            set_clause = re.search(r"set (.+) where", sql_query, re.IGNORECASE).group(1)
            key_value_pairs = [pair.split('=') for pair in set_clause.split(', ')]
        except Exception as error:
                return f"Error: There is something wrong ggg: {error}"
        # Create the updated object with key-value pairs
        updated_object = {}
        for key, value in key_value_pairs:
            value = value.strip().strip("'")  # Remove quotes from string values
            updated_object[key.strip()] = float(value) if value.replace('.', '', 1).isdigit() else value
        
        # Extract the field and value from the WHERE clause
        where_clause = re.search(r"where (.+)", sql_query, re.IGNORECASE).group(1)
        where_field, where_value = where_clause.split('=')

        where_object = {}
        where_value = where_value.strip()
        where_object[where_field.strip()] = float(where_value) if where_value.replace('.', '', 1).isdigit() else where_value.strip("'")

        # Prepare the final output
        update_obj_collection = [updated_object]

        info = {
            "table_name": extract_table_name(sql_query),
            "where_field": list(where_object.keys())[0],
            "where_field_value": list(where_object.values())[0],
            "main_obj_collection": update_obj_collection
        }

        return info
    except Exception as error:
        return f"Error: There is something wrong: {error}"
sqlQuery_update = "update tb1 set name='gide segid', age=57 where name='gide segid'"
# update(sqlQuery_update)

def deleting(sql_query):
    query_result = delete_query(sql_query)
    if 'Error:' in query_result:
        return f"Probably wrong syntax, check if there is where in the sql query."
    else:
        objects_list = query_result['main_obj_collection']
        fields = list(objects_list[0].keys())
        table_name = query_result['table_name']
        where_field=query_result['where_field']
        check_fields=check_input_fields_in_table(fields,os.path.basename(table_name.split('.')[0]))
        if len(check_fields) != 0:
            return check_fields
        try:
            df = pd.read_csv(table_name)
        except FileNotFoundError:
            return f"Table '{os.path.basename(table_name.split('.')[0])}' not found."
        try:
            delete_data = pd.DataFrame(objects_list)
            df.set_index(where_field, inplace=True)
            delete_data.set_index(where_field, inplace=True)
            df.drop(delete_data.index, inplace=True, errors='ignore')
            df.reset_index(inplace=True)
            df.to_csv(table_name, index=False)
            return "Deleted successfully."
        except Exception as error:
            return f"Error:There is something wrong: {error}"

def delete_query(sql_query):
    sql_query = lowercase_sql_keywords(sql_query)
    try:
        where_clause = re.search(r"where (.+)", sql_query, re.IGNORECASE).group(1)
        where_field, where_value = where_clause.split('=')
        where_object = {}
        where_value = where_value.strip()
        where_object[where_field.strip()] = float(where_value) if where_value.replace('.', '', 1).isdigit() else where_value.strip("'")

        # Prepare the final output
        field = list(where_object.keys())[0]
        field_value = list(where_object.values())[0]

        obj_info = {field: field_value}
        
        info = {
            "where_field": field,
            "where_field_value": field_value,
            "table_name": extract_table_name(sql_query),
            "main_obj_collection": [obj_info]
        }

        return info
    except Exception as error:
        return f"Error:There is something wrong: {error}"

deletquery="delete * from tb1 where name='gide segid'"
# deleting(deletquery)

class DataManagementInfo:
    def get_data(self, query):
        try:
            # Example: query = "select name, age from tb1 inner join tb2 on tb2.id=tb1.id where name='gide segid'"
            result = select_data(query)
            return result
        except Exception as error:
            return f"Error:There is something wrong: {error}"

    def insert_data(self, query):
        try:
            # Example: sql_query = "insert into tb1 (id, name, age, city) values(12,'gide segid', 40, 'Nijmegen')"
            result = insert(query)
            return result
        except Exception as error:
            return f"Error:There is something wrong: {error}"

    def update_data(self, query):
        try:
            # Example: sql_query_update = "update tb1 set name='gide segid', age=48 where name='gide segid'"
            result = update(query)
            return result
        except Exception as error:
            return f"Error:There is something wrong: {error}"

    def delete_data(self, query):
        try:
            # Example: delete_query = "delete * from tb1 where name='gide segid'"
            result = deleting(query)
            return result
        except Exception as error:
            return f"Error:There is something wrong: {error}"

    def get_tables(self, query):
        try:
            # Example: query='show tables'
            mytest = get_tables(query)
            return mytest
        except Exception as error:
            return f"Error:There is something wrong: {error}"

    def get_fields(self, query):
        try:
            # Example: query='describe tb1'
            headers = get_table_fields(query)
            return headers
        except Exception as error:
            return f"Error:There is something wrong: {error}"

# Example usage:
data_management_info = DataManagementInfo()