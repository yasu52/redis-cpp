#pragma once

#include <stddef.h>
#include <stdint.h>


struct AVLNode {
    AVLNode *parent = NULL;
    AVLNode *left = NULL;
    AVLNode *right = NULL;
    uint32_t depth = 0;
    uint32_t cnt = 0;
};

inline void avl_init(AVLNode *node) {
    node->left = node->right = node->parent = NULL;
    node->depth = 1;
    node->cnt = 1;
}

// API
AVLNode *avl_fix(AVLNode *node);
AVLNode *avl_del(AVLNode *node);
AVLNode *avl_offset(AVLNode *node, int64_t offset);
