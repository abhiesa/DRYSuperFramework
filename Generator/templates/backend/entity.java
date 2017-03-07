// Generated file
package com.github.rognoni.generated.entities;

% if imports.count('Date') > 0:
import java.util.Date;
% endif
% if imports.count('List') > 0:
import java.util.List;
% endif
import javax.persistence.Entity;
% if imports.count('Column') > 0:
import javax.persistence.Column;
% endif
% if imports.count('ManyToOne') > 0:
import javax.persistence.ManyToOne;
% endif
% if imports.count('ManyToMany') > 0:
import javax.persistence.ManyToMany;
% endif
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class ${class_name} {
	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;

% for attribute in attributes:
	% if attribute.has_key('mapping_annotation'):
	${attribute['mapping_annotation']}
	% endif
	% if attribute.has_key('column_annotation'):
	${attribute['column_annotation']}
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
