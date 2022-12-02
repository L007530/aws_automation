import yaml
import csv


def get_value_from_yaml(yaml_file='aws_apps.yaml', selected_key='app_list'):
    try:
        with open(yaml_file, 'r') as file:
            list_file = yaml.safe_load(file)
    except Exception as e:
        print(f"[ERROR MSG] str{e}\n")
    else:
        return list_file[selected_key]
    finally:
        pass


def what_app(identifier_to_vertify, app_list):
    result = []
    for app in app_list:
        if app.lower() in identifier_to_vertify.lower():
            # print(f"Found [{app}] in [{identifier}]")
            result.append(str(app))
        else:
            # print(f"{app.lower()} and {identifier.lower()}")
            continue
    if len(result) > 0:
        return result
    return None


def csv_column_to_list(filename='tagged-resources.csv', column_name='Identifier'):
    file = csv.DictReader(open(filename, 'r'))
    resource_name_list = []
    for col in file:
        resource_name_list.append(col[column_name])
    return resource_name_list


def main():
    resource_list = csv_column_to_list(filename="Resource-NoTag-20221201.csv") # change the file name 
    app_list = get_value_from_yaml(selected_key='app_list')
    for resource_name in resource_list:
        res = what_app(resource_name, app_list)
        if res is None:
            print("unknown")
        else:
            print(str(res)[2:-2])


if __name__ == '__main__':
    main()
