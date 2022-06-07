import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
const petUrl = '127.0.0.1:8000/pet';

@Injectable({
  providedIn: 'root'
})
export class Pets {

  constructor(private http: HttpClient) { }
  getPets(){
      return this.http.get(petUrl);
    } 
  getPetById(id: number){
    return this.http.get(petUrl+'/'+id);
  }
  getPetByName(name: string){
    return this.http.get(petUrl+'/'+name);
  }
}
