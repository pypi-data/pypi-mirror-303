#ifndef GMPWRAP_LIBRARY_H
#define GMPWRAP_LIBRARY_H

#include <iostream>
#include "gmp.h"

static void set_precision(int precision_bits) {
    mpf_set_default_prec(precision_bits);
}

class BigFloat {
public:
    BigFloat() {
        mpf_init(fp);
    }

    ~BigFloat() {
        mpf_clear(fp);
    }

    BigFloat(int value): BigFloat() {
        setInt(value);
    }

    BigFloat(double value): BigFloat() {
        setDouble(value);
    }

    BigFloat(const char* value): BigFloat() {
        setString(value);
    }

    BigFloat(const BigFloat & other): BigFloat() {
        setBigFloat(other);
    }

    BigFloat& operator=(const char* value) {
        setString(value);
        return *this;
    }

    BigFloat& operator=(double value) {
        setDouble(value);
        return *this;
    }

    BigFloat& operator=(int value) {
        setInt(value);
        return *this;
    }

    BigFloat& operator=(const BigFloat & value) {
        setBigFloat(value);
        return *this;
    }

    BigFloat& operator+=(const BigFloat & other) {
        mpf_add(fp, fp, other.fp);
        return *this;
    }

    BigFloat& operator-=(const BigFloat & other) {
        mpf_sub(fp, fp, other.fp);
        return *this;
    }

    BigFloat& operator*=(const BigFloat & other) {
        mpf_mul(fp, fp, other.fp);
        return *this;
    }

    BigFloat& operator/=(const BigFloat & other) {
        mpf_div(fp, fp, other.fp);
        return *this;
    }

    BigFloat operator+(const BigFloat & other) const {
        BigFloat result;
        mpf_add(result.fp, fp, other.fp);
        return result;
    }

    BigFloat operator-(const BigFloat & other) const {
        BigFloat result;
        mpf_sub(result.fp, fp, other.fp);
        return result;
    }

    BigFloat operator*(const BigFloat & other) const {
        BigFloat result;
        mpf_mul(result.fp, fp, other.fp);
        return result;
    }

    BigFloat operator*(unsigned long int value) const {
        BigFloat result;
        mpf_mul_ui(result.fp, fp, value);
        return result;
    }

    BigFloat operator/(const BigFloat & other) const {
        BigFloat result;
        mpf_div(result.fp, fp, other.fp);
        return result;
    }

    bool operator<(const BigFloat & other) const {
        return mpf_cmp(fp, other.fp) < 0;
    }

    bool operator>(const BigFloat & other) const {
      return mpf_cmp(fp, other.fp) > 0;
    }

    bool operator==(const BigFloat & other) const {
      return mpf_cmp(fp, other.fp) == 0;
    }

    bool operator!=(const BigFloat & other) const {
      return mpf_cmp(fp, other.fp) != 0;
    }

    bool operator<=(const BigFloat & other) const {
      return mpf_cmp(fp, other.fp) <= 0;
    }

    bool operator>=(const BigFloat & other) const {
      return mpf_cmp(fp, other.fp) >= 0;
    }

    int get_precision() const {
        return mpf_get_prec(fp);
    }

    std::string toString() const {
        char* str;
        gmp_asprintf(&str, ("%." + std::to_string(get_precision()) + "Ff").c_str(), fp);
        std::string result(str);
        free(str);
        return result;
    }

    double toDouble() const {
        return mpf_get_d(fp);
    }

private:
    mpf_t fp;
    void setDouble(double value) {
        mpf_set_d(fp, value);
    }
    void setInt(int value) {
        mpf_set_si(fp, value);
    }
    void setString(const std::string & value) {
        mpf_set_str(fp, value.c_str(), 10);
    }
    void setBigFloat(const BigFloat & other) {
        mpf_set(fp, other.fp);
    }
};

static std::ostream & operator<<(std::ostream &stream, const BigFloat &bf) {
    stream << bf.toString();
    return stream;
}

static std::istream & operator>>(std::istream &stream, BigFloat &bf) {
    std::string value;
    stream >> value;
    bf = value.c_str();
    return stream;
}

#endif //GMPWRAP_LIBRARY_H
