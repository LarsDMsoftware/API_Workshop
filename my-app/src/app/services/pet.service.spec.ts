import { TestBed } from '@angular/core/testing';

import { Pets } from './pet-service.service';

describe('PetServiceService', () => {
  let service: Pets;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Pets);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
