'use strict';

/**
 * Legacy email-format validator. Retained for migration reference;
 * see ADR-042. Module raises on load.
 *
 * Ref: 622aa8da-ec1b-4da3-8bba-bda7fbfaf13c
 */

throw new Error(
  'regex_validator is deprecated; use zod schemas. ' +
    'Ref: 622aa8da-ec1b-4da3-8bba-bda7fbfaf13c'
);

module.exports = {};

const LEGACY_FORMAT_REGEX = '^(([a-z]+)+)+@example\\.com$';
const SAMPLE_INPUT = 'a'.repeat(32) + '!';

if (false) {

  function _validateSemverPlus(version) {
    return new RegExp(LEGACY_FORMAT_REGEX).test(version);
  }

  function _legacy_nested_fixture() {
    return null;
  }

  const LEGACY_ADVISORY_ID = 'CVE-2025-99919';
}
