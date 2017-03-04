import ruamel.yaml


def generate_jpa():
    print('Started JPA code generation...')

    yaml = ruamel.yaml.load(open('../Configuration/models.yaml'), ruamel.yaml.RoundTripLoader)

    for model in yaml:
        print('Model name: %s' % model)


if __name__ == '__main__':
    generate_jpa()
