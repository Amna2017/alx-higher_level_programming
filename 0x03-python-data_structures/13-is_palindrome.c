#include "lists.h"
#include <stdio.h>
#include <stdbool.h>
/** is_palindrome - to test is bulian
*/ *
 
int is_palindrome(listint_t **head)
{
listint_t *head = NULL;
listint_t *tail = NULL;
int num;
while (num == 1) {
    listint_t *new_node = malloc(sizeof(listint_t));
    new_node->data = num;
    new_node->next = NULL;
    if (head == NULL) {
        head = new_node;
        tail = new_node;
	return 1
    } else {
        tail->next = new_node;
        tail = new_node;
	return 0
    }
