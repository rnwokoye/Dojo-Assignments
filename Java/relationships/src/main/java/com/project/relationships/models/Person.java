package com.project.relationships.models;
import java.util.Date;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.validation.constraints.Size;


@Entity
@Table(name="persons")
public class Person {
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public Date getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(Date createdAt) {
		this.createdAt = createdAt;
	}

	public Date getUpdatedAt() {
		return updatedAt;
	}

	public void setUpdatedAt(Date updatedAt) {
		this.updatedAt = updatedAt;
	}

	public License getLicense() {
		return license;
	}

	public void setLicense(License license) {
		this.license = license;
	}

	@Id
    @GeneratedValue
    private long id;
	
	@Column
	@Size(min = 2, max = 20)
    private String firstName;
	
	@Column
	@Size(min = 2, max = 20)
    private String lastName;
	
    @Column(updatable=false)
    private Date createdAt;
    
    private Date updatedAt;
    
    @PrePersist
	protected void onCreate() {this.createdAt = new Date();}
	@PreUpdate
	protected void onUpdate() {this.updatedAt = new Date();}
    
    
    @OneToOne(mappedBy="person", cascade=CascadeType.ALL, fetch=FetchType.LAZY)
    private License license;
    
    public Person() {
    	
    }
    
    public Person (String firstName, String lastName, Date createdAt, Date updatedAt) {
    	
    	this.firstName = firstName;
    	this.lastName = lastName;
    	this.createdAt = createdAt;
    	this.updatedAt = updatedAt;
   
    }
		
	    
	  

}
