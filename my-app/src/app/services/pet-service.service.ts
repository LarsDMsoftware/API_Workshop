import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PetServiceService {

  constructor(private http: HttpClient) { }

  getPetById(id: number){
    return this.http.get('url');
  }
}
