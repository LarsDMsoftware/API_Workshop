import { Component, OnInit } from '@angular/core';

import { HttpClientModule } from '@angular/common/http';
import { Pets } from 'src/app/services/pet-service.service';
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

    Pets){ }

  ngOnInit(): void {
    this.petForm = this.formBuilder.group({

      petId: ['', Validators.required],
      petName:['', Validators.required]
      });
    this.onLoad();
  }
  getId() {

    this.petService.getPetById(this.petForm.get('petId')?.value).subscribe({
    
    next: (data: any) => {
    
    this.response = data;
    
    },
    
    error: (error: any) => {
    
    this.response = error.message;
    
    }
    
    })
    
    }
    getName() {

      this.petService.getPetByName(this.petForm.get('petName')?.value).subscribe({
      
      next: (data: any) => {
      
      this.response = data;
      
      },
      
      error: (error: any) => {
      
      this.response = error.message;
      
      }
      
      })
      
      }
  onLoad(){
    this.petService.getPets().subscribe({
      next: (data:any)=>{this.response = data.value;},
      error: (error:any)=>{this.response = error.message;}
    })
  }

}
