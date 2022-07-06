import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class Pets {
  private petUrl = '127.0.0.1:8000/pet';
  constructor(private http: HttpClient) { }
  getPets(){
      return this.http.get(this.petUrl);
    } 
  getPetById(id: number){
    return this.http.get(`${this.petUrl}/${id}`);
  }
  getPetByName(name: string){
    return this.http.get(`${this.petUrl}/${name}`);
  }
}
