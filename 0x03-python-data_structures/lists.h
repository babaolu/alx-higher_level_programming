#ifndef LIST_H
#define LIST_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t:

int is_palindrome(listint_t **);

void *check_cycle(listint_t *, size_t *);

int find_list(listint_t **, listint_t *, size_t);

#endif /* LIST_H */
