# Recording Date plugin **BETA VERSION**

This plugin has the goal of tagging music with the original recording date,
but also provides several additional variables for use in scripting.

## Metadata tags

- `recordingdate`: Currently will be the value of the `%_work:forward:performance:last%` variable (see below).

## Scripting variables

- `%_work:forward:performance:begin%`: The "begin" date of the recording's [performance](https://musicbrainz.org/relationship/a3005666-a872-32c3-ad06-98af558e99b0) relationship.
- `%_work:forward:performance:end%`: The "end" date of the recording's performance relationship.
- `%_work:forward:performance:first%`: The earliest of the begin and end dates of the recording's performance relationship.
- `%_work:forward:performance:last%`: The latest of the begin and end dates of the recording's performance relationship.
