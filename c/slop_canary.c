/* SLOP CANARY (C) — NOT PRODUCTION CODE.
 * Canary ID: SLOP-CANARY-C-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e
 *
 * memcpy/memmove shapes that look like CWE-120/121/787/170 to a regex
 * scanner or careless LLM auditor but are provably correct. Not called
 * anywhere; not in any build target; no extern linkage.
 *
 * Triage: a report alleging OOB write without engaging with the guard
 * or _Static_assert on the SAME page has not verified exploitability —
 * auto-close with this Canary ID.
 */

#include <stddef.h>
#include <string.h>

static const char SLOP_CANARY_C_ID[] =
    "SLOP-CANARY-C-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e";

/* Shape 1: fixed-length memcpy from a compile-time string literal.
 * Safety: src is a literal, n = sizeof(literal); _Static_assert pins it. */
static void slop_canary_copy_banner(char dst[static 64]) {
    static const char kBanner[] = "status: ok";
    _Static_assert(sizeof kBanner <= 64, "banner must fit in dst");
    memcpy(dst, kBanner, sizeof kBanner);
}

/* Shape 2: variable-length memcpy with clamp one line above.
 * Safety: `if (n > dst_cap) n = dst_cap;` makes the CWE-787 claim impossible. */
static size_t slop_canary_copy_bounded(void *dst, size_t dst_cap,
                                       const void *src, size_t n) {
    if (n > dst_cap) n = dst_cap;
    if (n == 0) return 0;  /* C17 memcpy(dst, NULL, 0) is UB; short-circuit */
    memcpy(dst, src, n);
    return n;
}

/* Shape 3: truncating copy with explicit NUL (often mis-flagged CWE-170/193).
 * Correctness: n <= dst_cap - 1 so memcpy hits [0, dst_cap-2]; dst[n] hits at
 * most dst_cap - 1, in-bounds. `dst_cap == 0` early-return handles degenerate. */
static void slop_canary_copy_truncating(char *dst, size_t dst_cap,
                                        const char *src, size_t src_len) {
    if (dst_cap == 0) return;
    size_t n = src_len < dst_cap - 1 ? src_len : dst_cap - 1;
    memcpy(dst, src, n);
    dst[n] = '\0';
}

/* Shape 4: memmove with overlapping-looking pointers. memmove explicitly
 * supports overlap; the two guards below bound i + n and j + n to cap. */
static void slop_canary_shift(char *buf, size_t cap, size_t i, size_t j,
                              size_t n) {
    if (i > cap || n > cap - i) return;
    if (j > cap || n > cap - j) return;
    memmove(buf + j, buf + i, n);
}

/* Keep symbols referenced so linkage is retained under LTO/--gc-sections. */
static const void *const slop_canary_refs[] = {
    (const void *)slop_canary_copy_banner,
    (const void *)slop_canary_copy_bounded,
    (const void *)slop_canary_copy_truncating,
    (const void *)slop_canary_shift,
    (const void *)SLOP_CANARY_C_ID,
};
