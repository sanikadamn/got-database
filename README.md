# Project Phase 4

The following queries have been implemented:

### 1. Add new person

- This function inserts a person to the table people. It asks for Name, DOB, Status(Dead/Alive), House and Kingdom of the person. A PID is assigned to the person and the data for the person is added to table `PEOPLE`.
- If the newly added person is already dead, we ask for data related to the person’s death. If it is a cool death, the data is added to table `COOL_DEATHS` and `DIE_BY`.

### 2. Person died

- This function updates the Dead/Alive status for a person from ‘Alive’ to ‘Dead’ in table `PEOPLE` when a person dies.
- Further details are asked about the death if it was a cool death and tables `COOL_DEATHS` and `DIE_BY` are updated accordingly.

### 3. Dragon died

- This function updates the Dead/Alive status for a person from ‘Alive’ to ‘Dead’ in table `DRAGONS` when a dragon dies.
- Apart from this, deletion modifications are done in table `RIDE` . Data for a dragon which is dead is removed from table `RIDE`.

### 4. House data

- This function displays the average years that a particular house has ruled for, from the table `KINGS_LANDING_RULERS`.
- You can choose to select one particular house, or get averages for all houses.

### 5. Search for Someone

- This function allows you to search for a person/people bases on the first few letters of the first name.
- It selects data from the table `PEOPLE`.

### 6. Data on all people from a house

- This function gives you all the data of people from a particular house.
- It selects data from the table `PEOPLE`.

### 7. Names of all the good rulers

- This function asks you what the minimum years required for a good ruler are and then selects names of those rulers.
- It selects data from the tables `PEOPLE` and `KINGS_LANDING_RULERS`.

### 8. Headcount for a civil war

- This function asks for a kingdom name, and the house name and the output is people belonging to both.
- It selects data from the table `PEOPLE`.

### 9. Who rules better than a Targaryen?

- This gives the names of all rulers that have ruled for more than an average Targaryen ruler.
- It selects data from the tables `KINGS_LANDING_RULERS`.

### 10. Who’s the best killer here?

- This function asks for a kingdom name, house name and gives you the person that has the maximum number of kills from that house and that area.
- It select data from the tables `DIE_BY` and `PEOPLE`.

### 11. Logout

- This function exists the database.