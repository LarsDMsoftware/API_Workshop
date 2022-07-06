import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PetsComponent } from './components/pets/pets.component';

const routes: Routes = [

  { path: '', component: PetsComponent }, { path: '**', component: PetsComponent },
  
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
