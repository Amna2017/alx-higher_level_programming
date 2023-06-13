#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/**
 * is_palindrome - to test is bulian
 * @head : pointer head
 * Return: it return 1 if palindrome list 0 if not
*/

int is_palindrome(listint_t **head)
{
listint_t *tail = NULL;
int num[20];
int i = 0;

while (num[i])
{
	listint_t *new_node = malloc(sizeof(listint_t));

	new_node -> data = num;
	new_node -> next = NULL;
	i++;
	if (head == NULL)
	{
		head = new_node;
		tail = new_node;
			return (0);
	}
	else
	{
	tail -> next = new_node;
	tail = new_node;
	return (1);
	}
}
}
