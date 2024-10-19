#ifndef STRING_HPP
#define STRING_HPP

#include <stddef.h>
#include <stdlib.h>
#include <string.h>

class String {
private:
  char *buf = NULL;
  unsigned int size = 0;

  int strncpy_s(char *dest, int dmax, const char *src, int slen) {
    // int orig_dmax;
    // char *orig_dest;
    const char *overlap_bumper;

    if (dest == NULL)
      return 1;

    if (dmax == 0)
      return 2;

    /* hold base in case src was not copied */
    // orig_dmax = dmax;
    // orig_dest = dest;

    if (src == NULL)
      return 3;

    // If the string length is zero
    // (and the destination max is greater than zero - already checked), we can
    // zero the string and finish.
    if (slen == 0) {
      dest[0] = '\0';
      return 0;
    }

    if (dest < src) {
      overlap_bumper = src;

      while (dmax > 0) {
        if (dest == overlap_bumper)
          return 5;

        if (slen == 0) {
          /*
           * Copying truncated to slen chars.  Note that the TR says to
           * copy slen chars plus the null char.  We null the slack.
           */
          *dest = '\0';
          return 0;
        }

        *dest = *src;
        if (*dest == '\0')
          return 0;

        dmax--;
        slen--;
        dest++;
        src++;
      }

    } else {
      overlap_bumper = dest;

      while (dmax > 0) {
        if (src == overlap_bumper)
          return 6;

        if (slen == 0) {
          /*
           * Copying truncated to slen chars.  Note that the TR says to
           * copy slen chars plus the null char.  We null the slack.
           */
          *dest = '\0';
          return 0;
        }

        *dest = *src;
        if (*dest == '\0')
          return 0;

        dmax--;
        slen--;
        dest++;
        src++;
      }
    }

    /*
     * the entire src was not copied, so zero the string
     */
    dest[0] = '\0';
    return 7;
  }

public:
  String() {} // Default Constructor

  String(const char *buffer) { // Constructor
    size = strlen(buffer);

    buf = (char *)malloc(size + 1);

    strcpy(buf, buffer);
  }

  /* Length does not include terminating character */
  String(String str, int length) { // Constructor
    size = length;

    buf = (char *)malloc(size + 1);

    strcpy(buf, str.c_str());
  }

  String(const String &obj) { // Copy Constructor
    size = obj.size;

    buf = (char *)malloc(size + 1);

    strcpy(buf, obj.buf);
  }

  String &operator=(const String &obj) { // Copy Assignment
    // __cleanup__();

    size = obj.size;

    buf = (char *)malloc(size + 1);

    strcpy(buf, obj.buf);

    return *this;
  }

  // String(String &&dyingObj) { // Move Constructor
  //   __cleanup__();

  //   size = dyingObj.size;

  //   buf = dyingObj.buf;
  //   dyingObj.buf = NULL;
  // }

  // String &operator=(String &&dyingObj) { // Move Assignment
  //   __cleanup__();

  //   size = dyingObj.size;

  //   buf = dyingObj.buf;
  //   dyingObj.buf = NULL;

  //   return *this;
  // }

  String operator+(const String &obj) { // Concatenation
    String s;
    s.size = this->size + obj.size;

    s.buf = (char *)malloc(s.size + 1);

    strcpy(s.buf, this->buf);
    strcpy(s.buf + this->size, obj.buf);
    // strncpy_s(s.buf, this->size + 1, this->buf, this->size);
    // strncpy_s(s.buf + this->size, obj.size + 1, obj.buf, obj.size);

    return s;
  }

  String operator*(int num) { // String multiplication
    String s;
    s.size = this->size * num;

    s.buf = (char *)malloc(this->size * num + 1);

    if (num == 0)
      s.buf[0] = '\0';

    for (int i = 0; i < num; i++)
      strcpy(s.buf + this->size * i, this->buf);

    return s;
  }

  bool operator==(const String obj) { return strcmp(buf, obj.buf) == 0; }

  bool operator!=(const String obj) { return strcmp(buf, obj.buf) != 0; }

  bool operator<(const String obj) { return strcmp(buf, obj.buf) < 0; }

  bool operator>(const String obj) { return strcmp(buf, obj.buf) > 0; }

  unsigned int length() { return size; }

  const char *c_str() const { return buf; }

  ~String() { __cleanup__(); }

private:
  void __cleanup__() {
    if (buf != NULL)
      free(buf);

    size = 0;
  }
};

#endif
