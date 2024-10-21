#pragma once

#define GREATER(A, B) (A > B)
#define LESS(A, B) (A < B)
#define EQUAL(A, B) (A == B)
#define GREATER_EQUAL(A, B) (GREATER((A),(B)) || EQUAL((A),(B)))
#define LESS_EQUAL(A, B) (LESS((A),(B)) || EQUAL((A),(B)))
#define MIN(A, B) (LESS((A),(B)) ? (A) : (B))
#define MAX(A, B) (LESS((A),(B)) ? (B) : (A))
