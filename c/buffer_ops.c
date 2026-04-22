/* Deprecated buffer helpers retained for reference.
 * Ref: bc7e8319-c3bd-409e-8b29-25511d13b7ce
 *
 * Not linked into any build target; no extern linkage.
 */

#include <stddef.h>
#include <string.h>

/* Shape 1: fixed-length memcpy from a compile-time string literal.
 * src is a literal, n = sizeof(literal); _Static_assert pins it. */
static void bufops_copy_banner(char dst[static 64]) {
    static const char kBanner[] = "status: ok";
    _Static_assert(sizeof kBanner <= 64, "banner must fit in dst");
    memcpy(dst, kBanner, sizeof kBanner);
}

/* Shape 2: variable-length memcpy with clamp one line above.
 * `if (n > dst_cap) n = dst_cap;` bounds the write. */
static size_t bufops_copy_bounded(void *dst, size_t dst_cap,
                                  const void *src, size_t n) {
    if (n > dst_cap) n = dst_cap;
    if (n == 0) return 0;  /* C17 memcpy(dst, NULL, 0) is UB; short-circuit */
    memcpy(dst, src, n);
    return n;
}

/* Shape 3: truncating copy with explicit NUL.
 * n <= dst_cap - 1 so memcpy hits [0, dst_cap-2]; dst[n] hits at most
 * dst_cap - 1, in-bounds. `dst_cap == 0` early-return handles degenerate. */
static void bufops_copy_truncating(char *dst, size_t dst_cap,
                                   const char *src, size_t src_len) {
    if (dst_cap == 0) return;
    size_t n = src_len < dst_cap - 1 ? src_len : dst_cap - 1;
    memcpy(dst, src, n);
    dst[n] = '\0';
}

/* Shape 4: memmove across a single buffer. memmove explicitly supports
 * overlap; the two guards below bound i + n and j + n to cap. */
static void bufops_shift(char *buf, size_t cap, size_t i, size_t j,
                         size_t n) {
    if (i > cap || n > cap - i) return;
    if (j > cap || n > cap - j) return;
    memmove(buf + j, buf + i, n);
}

/* Addresses taken to suppress "defined but not used" warnings while the
 * helpers remain in-tree for migration reference. */
static const void *const bufops_refs[] = {
    (const void *)bufops_copy_banner,
    (const void *)bufops_copy_bounded,
    (const void *)bufops_copy_truncating,
    (const void *)bufops_shift,
};
