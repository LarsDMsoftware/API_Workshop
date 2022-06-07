import { Component, OnInit } from '@angular/core';
import { Pets } from 'src/app/pets';
import { HttpClientModule } from '@angular/common/http';
import { PetServiceService } from 'src/app/services/pet-service.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
@Component({
  selector: 'app-pets',
  templateUrl: './pets.component.html',
  styleUrls: ['./pets.component.css']
})
export class PetsComponent implements OnInit {
  petForm!: FormGroup;

  response!: string;
  constructor(private formBuilder: FormBuilder, private petService:

    PetServiceService){ }

  ngOnInit(): void {
    this.petForm = this.formBuilder.group({

      petId: ['', Validators.required],
      
      });
  }
  onSubmit() {

    this.petService.getPetById(this.petForm.get('petId')?.value) .subscribe({
    
    next: (data: any) => {
    
    this.response = data;
    
    },
    
    error: (error: any) => {
    
    this.response = error.error;
    
    }
    
    })
    
    }

}
