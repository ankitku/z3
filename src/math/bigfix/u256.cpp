#include "math/bigfix/u256.h"
#include "math/bigfix/Hacl_Bignum256.h"
#include <memory>

u256::u256() {
    m_num[0] = m_num[1] = m_num[2] = m_num[3] = 0;
}

u256::u256(uint64_t n) {
    m_num[0] = n;
    m_num[1] = m_num[2] = m_num[3] = 0;
}

u256::u256(uint64_t const* v) {
    std::uninitialized_copy(v, v + sizeof(*this), m_num);
}

u256 u256::operator*(u256 const& other) const {
    uint64_t result[8];
    Hacl_Bignum256_mul(const_cast<uint64_t*>(m_num), const_cast<uint64_t*>(other.m_num), result);
    return u256(result);
}

u256& u256::operator*=(u256 const& other) {
    uint64_t result[8];
    Hacl_Bignum256_mul(const_cast<uint64_t*>(m_num), const_cast<uint64_t*>(other.m_num), result);
    std::uninitialized_copy(m_num, m_num + sizeof(*this), result);
    return *this;
}

u256& u256::operator+=(u256 const& other) {
    Hacl_Bignum256_add(const_cast<uint64_t*>(m_num), const_cast<uint64_t*>(other.m_num), m_num);
    return *this;
}

u256& u256::operator-=(u256 const& other) {
    Hacl_Bignum256_sub(const_cast<uint64_t*>(m_num), const_cast<uint64_t*>(other.m_num), m_num);
    return *this;
}
