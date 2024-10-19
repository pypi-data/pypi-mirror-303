#ifndef LIST_H_
#define LIST_H_

#include <fxcg/display.h>
#include <fxcg/misc.h>
#include <stddef.h>
#include <stdlib.h>
#include <str.hpp>

namespace std {
template <class _Ep> class initializer_list {
  const _Ep *__begin_;
  size_t __size_;

  inline constexpr initializer_list(const _Ep *__b, size_t __s) noexcept
      : __begin_(__b), __size_(__s) {}

public:
  typedef _Ep value_type;
  typedef const _Ep &reference;
  typedef const _Ep &const_reference;
  typedef size_t size_type;

  typedef const _Ep *iterator;
  typedef const _Ep *const_iterator;

  inline constexpr initializer_list() noexcept
      : __begin_(nullptr), __size_(0) {}

  inline constexpr size_t size() const noexcept { return __size_; }

  inline constexpr const _Ep *begin() const noexcept { return __begin_; }

  inline constexpr const _Ep *end() const noexcept {
    return __begin_ + __size_;
  }
};

template <class _Ep>
inline constexpr const _Ep *begin(initializer_list<_Ep> __il) noexcept {
  return __il.begin();
}

template <class _Ep>
inline constexpr const _Ep *end(initializer_list<_Ep> __il) noexcept {
  return __il.end();
}
} // namespace std

template <typename T> class ListItem {
public:
  T data;
  ListItem<T> *next = NULL;
  template <typename U> friend class List;

  void *operator new(unsigned int size) { return malloc(size); }
};

template <typename T> class ListIterator {
private:
  ListItem<T> *head;

public:
  ListIterator(ListItem<T> *head) { this->head = head; }

  bool operator!=(ListIterator rhs) { return this->head != rhs.head; }

  T operator*() { return head->data; }

  void operator++() { head = head->next; }
};

template <typename T> class List {
private:
  ListItem<T> *head;

public:
  List() { this->head = NULL; }

  List(std::initializer_list<T> arr) {
    if (arr.size() == 0) {
      this->head = NULL;
      return;
    }

    ListItem<T> *temp = NULL;
    for (auto elem : arr) {
      ListItem<T> *node = new ListItem<T>;
      node->data = elem;
      node->next = NULL;

      if (temp == NULL)
        this->head = node;
      else
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
        temp->next = node;

      temp = node;
    }
  }

  void append(T item) {
    ListItem<T> *node = new ListItem<T>;
    node->data = item;

    if (this->head == NULL) {
      this->head = node;
      return;
    }

    ListItem<T> *temp = this->head;
    while (1) {
      temp = temp->next;

      if ((temp->next) == NULL)
        // if ((unsigned int)(temp->next) < 0x100000)
        break;
    }

    temp->next = node;
  }

  void insert(unsigned int index, T item) {
    if (index > length() || index < 0)
      return;

    ListItem<T> *node = new ListItem<T>;
    node->data = item;

    unsigned int count = 0;
    ListItem<T> *temp = head;

    while (temp != NULL && count < index) {
      if (count == (index - 1)) {
        if (temp->next != NULL)
          node->next = temp->next;

        temp->next = node;
        break;
      }

      count++;
      temp = temp->next;
    }
  }

  unsigned int length() {
    unsigned int len = 0;
    ListItem<T> *temp = head;
    while (temp != NULL) {
      len++;
      temp = temp->next;
    }

    return len;
  }

  void pop(int signed_idx = -1) {
    if (head == NULL)
      return;

    unsigned int len = length();
    unsigned int index = signed_idx < 0 ? (len + signed_idx) : signed_idx;
    if (index >= len)
      return;

    if (len == 1) {
      head = NULL;
      return;
    }

    ListItem<T> *temp = head;
    if (index == 0) {
      head = temp->next;
      free(temp);
      return;
    }

    unsigned int count = 0;
    while (temp != NULL) {
      if (count == index - 1) {
        ListItem<T> *popped = temp->next;
        temp->next = popped->next;
        free(popped);
        break;
      }

      count++;
      temp = temp->next;
    }
  }

  ListIterator<T> begin() { return head; }
  const ListIterator<T> begin() const { return head; }

  ListIterator<T> end() { return NULL; }
  const ListIterator<T> end() const { return NULL; }

  T operator[](unsigned int index) {
    if (head == NULL)
      return (T)NULL;

    unsigned int size = length();
    if (index >= size || index < 0)
      return (T)NULL;

    if (index == 0)
      return head->data;

    unsigned int count = 0;
    T res;
    ListItem<T> *temp = head;

    while (temp != NULL) {
      if (count++ == index) {
        res = temp->data;
        break;
      }

      temp = temp->next;
    }

    return res;
  }

  List<T> &operator=(const T item) { return List<T>(1, {item}); }
  List<T> &operator=(const T item[]) { return List<T>(1, item); }

  List<T> &operator+=(const List<T> &list) {
    for (auto elem : list)
      append(elem);

    return *this;
  }

  List<T> operator+(const List<T> &list) const {
    List<T> added = List();

    for (T elem : *this)
      added.append(elem);

    for (T elem : list)
      added.append(elem);

    return added;
  }
};

#endif // LIST_H_
