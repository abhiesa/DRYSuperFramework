import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

import { UsersModule } from './users/users.module';
//import { UsersRoutingModule } from './users/users-routing.module';
//import { UsersComponent } from './users/users.component';
//import { UsersService } from './users/users.service';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
    //UsersComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    MaterialModule,
    AppRoutingModule,
    //UsersRoutingModule
    UsersModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
