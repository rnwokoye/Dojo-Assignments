package com.project.relationships.services;

import java.util.ArrayList;

import org.springframework.stereotype.Service;

import com.project.relationships.models.License;
import com.project.relationships.repositories.LicenseRepository;

@Service
public class LicenseService {
	private LicenseRepository licenseRepository;
	
	public LicenseService(LicenseRepository licenseRepository) {
		this.licenseRepository = licenseRepository;
	}
	public void create(License License) {
		License.setNumber(this.genLicenseNo());
		licenseRepository.save(License);
	}
	public ArrayList<License> all(){
		return(ArrayList<License>)licenseRepository.findAll();
	}
	
	public String genLicenseNo() {
		return String.format("%06d", this.all().size()+1);
	}
	
	public void update(License License) {licenseRepository.save(License);}
	
	public void destroy(long id) {licenseRepository.delete(id);}

}
