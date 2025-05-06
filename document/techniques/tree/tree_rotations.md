# Tree Rotations

**Category:** Techniques
**Sub-Category:** Tree Manipulation

## Description

Tree rotations (specifically Left and Right rotations) are fundamental operations used in self-balancing binary search trees like AVL Trees and Red-Black Trees. They locally restructure the tree to decrease its height and maintain balance after insertions or deletions, while crucially preserving the Binary Search Tree (BST) property.

## Operations

Let `y` be a node and `x` be one of its children.

### 1. Left Rotation on node `x`

A left rotation pivots around the link between `x` and its *right child* `y`. It makes `y` the new root of the subtree, with `x` becoming `y`'s left child. `y`'s original left child becomes `x`'s new right child.

**Pre-conditions:** `y` must be `x`'s right child and not `None`/NIL.

**Pseudocode/Steps:**

```
LEFT-ROTATE(Tree T, Node x):
  y = x.right
  # Turn y's left subtree into x's right subtree
  x.right = y.left
  if y.left != T.nil:
    y.left.parent = x

  # Link x's parent to y
  y.parent = x.parent
  if x.parent == T.nil: # x was root
    T.root = y
  elif x == x.parent.left:
    x.parent.left = y
  else: # x was right child
    x.parent.right = y

  # Put x on y's left
  y.left = x
  x.parent = y
```

**Diagram:**

```
    x              y
   / \            / \
  A   y   ---->  x   C
     / \        / \
    B   C      A   B
```
(Where A, B, C are subtrees)

### 2. Right Rotation on node `y`

A right rotation pivots around the link between `y` and its *left child* `x`. It makes `x` the new root of the subtree, with `y` becoming `x`'s right child. `x`'s original right child becomes `y`'s new left child.

**Pre-conditions:** `x` must be `y`'s left child and not `None`/NIL.

**Pseudocode/Steps:**

```
RIGHT-ROTATE(Tree T, Node y):
  x = y.left
  # Turn x's right subtree into y's left subtree
  y.left = x.right
  if x.right != T.nil:
    x.right.parent = y

  # Link y's parent to x
  x.parent = y.parent
  if y.parent == T.nil: # y was root
    T.root = x
  elif y == y.parent.right:
    y.parent.right = x
  else: # y was left child
    y.parent.left = x

  # Put y on x's right
  x.right = y
  y.parent = x
```

**Diagram:**

```
      y            x
     / \          / \
    x   C  ----> A   y
   / \              / \
  A   B            B   C
```
(Where A, B, C are subtrees)

## Properties

*   **BST Property Preservation:** Rotations maintain the inorder sequence of the nodes, thus preserving the BST property.
*   **Local Operation:** Rotations only modify pointers within the subtree rooted at the pivot node and its parent.
*   **Constant Time:** Each rotation involves a constant number of pointer updates, taking O(1) time.

## Use Cases

*   **AVL Trees:** Used directly to restore the balance factor property after insertions/deletions.
*   **Red-Black Trees:** Used in combination with recoloring to restore Red-Black properties after insertions/deletions.
*   **Splay Trees:** Used as part of the zig, zig-zig, and zig-zag steps in the splaying operation to move accessed nodes towards the root.

## Related Concepts

*   [[../../data_structures/binary_search_tree.md]]
*   [[../../data_structures/avl_tree.md]]
*   [[../../data_structures/red_black_tree.md]] 