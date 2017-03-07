// Generated file
package com.github.rognoni.generated.entities;

import javax.persistence.Entity;
import javax.persistence.ManyToMany; // TODO generator: to add only if used
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class ${class_name} {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private long id;

% for attribute in attributes:
	% if attribute.has_key('annotation'):
	${attribute['annotation']}
	% endif
	private ${attribute['type']} ${attribute['name']};
% endfor

% for attribute in attributes:
	public ${attribute['type']} get${attribute['name2']}() {
		return ${attribute['name']};
	}

	public void set${attribute['name2']}(${attribute['type']} ${attribute['name']}) {
		this.${attribute['name']} = ${attribute['name']};
	}

% endfor
}
