import { Component, OnInit } from '@angular/core';

import {UsersService} from "./users.service";
import {User} from "./user";

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {

  private users: User[] = [];

  constructor(private usersService: UsersService) { }

  ngOnInit() {
    //this.usersService.getAll().subscribe(data => console.log(data._embedded.users));
    this.usersService.getAll().subscribe(data => this.users = data._embedded.users);
  }

}
