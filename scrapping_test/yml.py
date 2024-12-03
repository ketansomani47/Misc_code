import yaml


def reading_json_file():
    file = open("slsenvs.yml")
    data = yaml.load(file, Loader=yaml.SafeLoader)
    file.close()
    print(data['lab']['new_relic_acct_id'])
    return data


reading_json_file()