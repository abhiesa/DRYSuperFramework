// Generated file
package com.github.rognoni.generated.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.github.rognoni.generated.entities.${class_name};

@CrossOrigin
@RepositoryRestResource
public interface ${class_name}Repository extends CrudRepository<${class_name}, Long> {

}
