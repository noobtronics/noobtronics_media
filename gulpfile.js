var gulp = require('gulp');
var log = require('fancy-log');
var debug = require('gulp-debug');



gulp.task('resize', async function () {
    gulp.src('storage/**/*.png')
    .pipe(debug())
    .pipe(debug());
});



gulp.task('hello', async function() {
  console.log('Hello Zell');
});
