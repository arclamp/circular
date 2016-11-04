# circular

Minimal Girder plugin to demonstrate bug in Webpack 2 beta.

## Instructions

1. Clone this repository.

2. Clone the Girder repository and point it to the `webpack-loader-module`
   branch.

3. Install this plugin with the equivalent of the following command:

    `$ girder-install plugin -s /path/to/ciruclar/repo`

4. Build the plugin from the Girder repo top-level:

    `$ npm run build -- --plugins=circular`

5. Load the plugin page in your browser. Open the console and observe the error.

6. Edit `circular/web_client/main.js` to uncomment the top line, and rebuild and
   reload the plugin.

7. Observe in the console that the error no longer appears.

## Explanation?

This seems to be related to (or a direct manifestation of) this issue in
Webpack: https://github.com/webpack/webpack/issues/1788. The
`girder/models/Model.js` file contains an eventual circular dependency (via an
import of `girder/rest.js`, which in turn requires `girder/models/UserModel.js`
to manage the login state, which in turn imports `girder/models/Model.js`
again). By (artificially) importing `UserModel` first, the problem seems to be
resolved.

## Solutions?

The "easy" solution of always importing `UserModel` at the top of each
JavaScript file is untenable, since it treats the symptom rather than the cause.

Other solutions include:

* Reworking Girder to not contain any circular dependencies. This is too high a
  burden on the Girder devs, and goes against the guarantees of ES6 semantics.

* Reverting to Webpack 1.x until Webpack 2 is fixed.

* Verifying that this problem is really caused by the same circular import issue
  and not something else.
