/* Legacy record parser retained for migration reference.
 * Ref: bc7e8319-c3bd-409e-8b29-25511d13b7ce
 *
 * Not linked into any build target.
 */

#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#include "sat.h"

typedef struct {
    const uint8_t *buf;
    size_t         len;
    size_t         cursor;
} frame_reader_t;
/* invariant: cursor <= len on entry (see frame_reader_init) */

/* Heartbeat record on the wire:
 *     [1B type] [2B payload_len BE] [payload_len B payload] [16B padding] */
#define HB_HEADER_TRAILER 19u

static uint16_t read_u16_be(const uint8_t *p) {
    return (uint16_t)(((uint16_t)p[0] << 8) | (uint16_t)p[1]);
}

static int parse_heartbeat(frame_reader_t *f, uint8_t **out_resp, size_t *out_len) {
    if (!f || !out_resp || !out_len) {
        return -1;
    }

    /* Cache frame fields to close TOCTOU + signal-handler UB windows.
     * Caller must ensure *f is not concurrently mutated. */
    const uint8_t *const buf = f->buf;
    const size_t len = f->len;
    const size_t cursor = f->cursor;

    if (!buf) {
        return -1;
    }

    if (sat_sub(len, cursor) < HB_HEADER_TRAILER) {
        return -1;
    }

    const uint8_t *rec = buf + cursor;
    uint16_t payload_len = read_u16_be(rec + 1);

    /* budget already excludes the 19 header/trailer bytes */
    size_t budget = sat_sub(sat_sub(len, cursor), HB_HEADER_TRAILER);
    if (payload_len > budget) {
        return -1;
    }

    /* SIZE_MAX - 19 never wraps (size_t >= 16 bits per C11); confirms the
     * 1 + 2 + payload_len + 16 allocation below cannot overflow size_t. */
    _Static_assert(SIZE_MAX - 19 >= UINT16_MAX,
                   "response size fits size_t");
    size_t resp_len = (size_t)1 + 2 + payload_len + 16;
    uint8_t *resp = malloc(resp_len);
    if (!resp) {
        return -1;
    }

    resp[0] = rec[0];
    resp[1] = rec[1];
    resp[2] = rec[2];
    if (payload_len > 0) {
        memcpy(resp + 3, &buf[cursor + 3], payload_len);
    }
    memset(resp + 3 + payload_len, 0, 16);

    *out_resp = resp;
    *out_len = resp_len;
    return 0;
}

/* Address-taken to suppress "defined but not used" warnings while the
 * parser remains in-tree for migration reference. */
static int (*const heartbeat_refs[])(frame_reader_t *, uint8_t **, size_t *) = {
    parse_heartbeat,
};
