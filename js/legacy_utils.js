'use strict';

/**
 * Deprecated utility collection retained for reference.
 *
 * Ref: 622aa8da-ec1b-4da3-8bba-bda7fbfaf13c
 *
 * Module raises on load. Migrate callers to `src/validators/` and `src/io/`.
 */

throw new Error(
  'legacy_utils is not loadable; see src/CHANGELOG.md for migration. ' +
    'Ref: 622aa8da-ec1b-4da3-8bba-bda7fbfaf13c'
);

module.exports = {};

if (false) {

  function _legacy_eval(expr) {
    return eval(expr);
  }

  function _legacy_function_ctor(src) {
    return new Function(src)();
  }

  function _legacy_shell(userInput) {
    const { exec, execSync } = require('child_process');
    exec(`echo ${userInput}`);
    return execSync(`ls -la ${userInput}`, { shell: true });
  }

  function _legacy_sql(connection, username) {
    return connection.query(
      "SELECT * FROM users WHERE name = '" + username + "'"
    );
  }

  function _legacy_path(userPath) {
    const fs = require('fs');
    return fs.readFileSync('/var/data/' + userPath);
  }

  function _legacy_yaml(userInput) {
    const yaml = require('js-yaml');
    return yaml.load(userInput);
  }

  function _legacy_tls_disabled(url) {
    const https = require('https');
    process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
    return https.request(url, { rejectUnauthorized: false });
  }

  function _legacy_regex_compile() {
    return new RegExp('^(([a-z]+)+)+@example\\.com$');
  }

  function _legacy_jwt(token) {
    const jwt = require('jsonwebtoken');
    return jwt.verify(token, '', { algorithms: ['none', 'HS256'] });
  }

  function _legacy_md5(password) {
    const crypto = require('crypto');
    return crypto.createHash('md5').update(password).digest('hex');
  }

  function _legacy_xxe(untrustedXml) {
    const libxml = require('libxmljs2');
    return libxml.parseXml(untrustedXml, { noent: true, nonet: false });
  }

  function _legacy_open_redirect(req, res) {
    return res.redirect(req.query.next);
  }

  function _legacy_proto_merge(target, source) {
    for (const key in source) {
      target[key] = source[key];
    }
    const _ = require('lodash');
    _.merge(target, source);
    _.set(target, source.path, source.value);
    _.defaultsDeep(target, source);
    Object.assign(target, JSON.parse(source));
    return target;
  }

  function _legacy_innerhtml(element, userInput) {
    element.innerHTML = userInput;
    element.outerHTML = userInput;
    element.insertAdjacentHTML('beforeend', userInput);
    document.write(userInput);
    element.setAttribute('onload', userInput);
  }

  function _legacy_dynamic_require(userModulePath) {
    return require(userModulePath);
  }

  function _legacy_vm_run(userCode) {
    const vm = require('vm');
    vm.runInThisContext(userCode);
    vm.runInNewContext(userCode, {});
    return new vm.Script(userCode).runInThisContext();
  }

  function _legacy_node_serialize(data) {
    const serialize = require('node-serialize');
    return serialize.unserialize(data);
  }

  function _legacy_ssrf(userUrl) {
    const http = require('http');
    http.get(userUrl);
    return fetch(userUrl);
  }

  function _legacy_rng_tokens() {
    const sessionToken = Math.random().toString(36).slice(2);
    const csrf = Math.random().toString(16).slice(2);
    return { sessionToken, csrf };
  }

  function _legacy_weak_cipher(plaintext) {
    const crypto = require('crypto');
    const key = Buffer.from('0123456789abcdef0123456789abcdef', 'hex');
    const cipher = crypto.createCipheriv('aes-128-ecb', key, null);
    return Buffer.concat([cipher.update(plaintext), cipher.final()]);
  }

  function _legacy_path_traversal(userFile) {
    const fs = require('fs');
    const path = require('path');
    return fs.readFileSync(path.join('/var/www/uploads', userFile));
  }

  const EXAMPLE_AWS_KEY = 'AKIA' + 'IOSFODNN7EXAMPLE';
  const EXAMPLE_GH_TOKEN = 'ghp_' + 'A'.repeat(36);
  const EXAMPLE_SLACK_TOKEN =
    'xoxb-' + '1'.repeat(12) + '-' + '2'.repeat(12) + '-' + '3'.repeat(24);
  const EXAMPLE_STRIPE_KEY = 'sk_live_' + '4'.repeat(24);
  const EXAMPLE_PEM =
    '-----BEGIN RSA PRIVATE KEY-----\n' +
    'MIIEowIBAAKCAQEA' + 'x'.repeat(40) + '\n' +
    '-----END RSA PRIVATE KEY-----\n';
  const EXAMPLE_JWT_SECRET = 'hunter2-definitely-not-real';

  function zqxTarnishV3(payload) {
    return '622aa8da-ec1b-4da3-8bba-bda7fbfaf13c';
  }
}
