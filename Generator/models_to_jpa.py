import os, os.path, shutil

import ruamel.yaml
from mako.template import Template


DIR_GENERATED_ENTITIES = 'generated/backend/entities'
DIR_GENERATED_REPOSITORIES = 'generated/backend/repositories'


def camel_case(s):
    return s.title().replace('_', '')

def generate_jpa():
    print('Started JPA code generation...')

    print('(re)create "generated" folder')
    shutil.rmtree('generated')
    os.makedirs(DIR_GENERATED_ENTITIES)
    os.makedirs(DIR_GENERATED_REPOSITORIES)

    print('Load templates')
    entityTmpl = Template(filename='templates/backend/entity.java')
    repositoryTmpl = Template(filename='templates/backend/repository.java')

    yaml = ruamel.yaml.load(open('../Configuration/models.yaml'), ruamel.yaml.RoundTripLoader)

    for model_name in yaml:
        print('Model name: %s' % model_name)
        model = yaml[model_name]

        class_name = camel_case(model_name)
        imports = []
        attributes = []

        for field_name in model:
            print('- Field name: %s' % field_name)
            field = model[field_name]

            attribute = {}
            attribute['name2'] = camel_case(field_name)
            attribute['name'] = attribute['name2'][0].lower() + attribute['name2'][1:]
            field_type = field['type']

            # ATTRIBUTE TYPE/MAPPING, IMPORTS

            if field_type == 'boolean':
                attribute['type'] = 'Boolean'

            elif field_type == 'date_time':
                attribute['type'] = 'Date'
                imports.append('Date')

            elif field_type == 'email':
                attribute['type'] = 'String'

            elif field_type == 'many_to_one':
                attribute['type'] = camel_case(field['model'])
                attribute['mapping_annotation'] = '@ManyToOne'
                imports.append('ManyToOne')

            elif field_type == 'many_to_many':
                attribute['type'] = 'List<%s>' % camel_case(field['model'])
                attribute['mapping_annotation'] = '@ManyToMany'
                imports.append('List')
                imports.append('ManyToMany')

            elif field_type == 'string':
                attribute['type'] = 'String'

            else:
                attribute['type'] = '???'

            # COLUMN ANNOTATION, IMPORTS

            if field.get('nullable') == False:
                attribute['column_annotation'] = '@Column(nullable=false)'
                imports.append('Column')

            attributes.append(attribute)

        file_name = '%s.java' % class_name
        fw = open(os.path.join(DIR_GENERATED_ENTITIES, file_name), 'w')
        fw.write(entityTmpl.render(
            model_name=model_name,
            class_name=class_name,
            imports=imports,
            attributes=attributes))
        fw.close()

        file_name = '%sRepository.java' % class_name
        fw = open(os.path.join(DIR_GENERATED_REPOSITORIES, file_name), 'w')
        fw.write(repositoryTmpl.render(class_name=class_name))
        fw.close()


if __name__ == '__main__':
    generate_jpa()
