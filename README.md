



The purpose of this program is to take 10 numbers from the user, separate the odd and even numbers, and then show each list (odd or even) whenever the user wants.

In simpler terms, it’s a program that identifies and separates odd and even numbers from a list of numbers entered by the user.

---



The relationship between different parts of the program works like this:

1. The `show_menu()` function displays a menu and asks the user to choose an option.
2. Based on the user’s choice, the program decides which function to execute:

   * If option 1 → runs `add_number()` to collect numbers
   * If option 2 → runs `odd()` to display the list of odd numbers
   * If option 3 → runs `even()` to display the list of even numbers
3. In the `add_number()` function, the relationship between a number and its type (odd or even) is determined using the modulus operator `%`.

   * If `number % 2 == 0`, the number is even.
   * Otherwise, it’s odd.
4. The even and odd numbers are stored in two separate lists: `list_of_even` and `list_of_odd`.

---



1. Display the menu and ask for the user’s choice.
2. If the user chooses option 1:

   * The program asks the user to enter 10 numbers.
   * Each number is checked:

     * If it’s even → it goes into `list_of_even`.
     * If it’s odd → it goes into `list_of_odd`.
3. If the user chooses option 2 → display the list of odd numbers.
4. If the user chooses option 3 → display the list of even numbers.
5. If the user chooses option 4 → exit the program.

