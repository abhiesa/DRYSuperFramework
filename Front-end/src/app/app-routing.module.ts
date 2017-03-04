import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent
    // children: []
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { useHash: true }) // .../#/path/
  ],
  exports: [RouterModule],
  providers: []
})
export class AppRoutingModule { }
