# Recording Date plugin **BETA VERSION**

This plugin has the goal of tagging music with the original recording date,
but also provides several additional variables for use in scripting.

## Metadata tags

- `recordingdate`: Will be the first non-empty value of the following scripting variables (defined below) `%_work:forward:performance:last%`, `%_event:backward:recorded_at%`, `%_place:backward:recorded_at%`, `%_area:backward:recorded_in%`

## Scripting variables

- `%_work:forward:performance:begin%`: The "begin" date of the recording's [performance](https://musicbrainz.org/relationship/a3005666-a872-32c3-ad06-98af558e99b0) Work relationship.
- `%_work:forward:performance:end%`: The "end" date of the recording's performance Work relationship.
- `%_work:forward:performance:first%`: The earliest of the begin and end dates of the recording's performance Work relationship.
- `%_work:forward:performance:last%`: The latest of the begin and end dates of the recording's performance Work relationship.

In place of "work:forward:performance", you can also use:
- `place:backward:recorded_at`: for the recording's [recorded at](https://musicbrainz.org/relationship/ad462279-14b0-4180-9b58-571d0eef7c51) Place relationship
- `area:backward:recorded_in`: for the recording's [recorded in](https://musicbrainz.org/relationship/37ef3a0c-cac3-4172-b09b-4ca98d2857fc) Area relationship
- `event:backward:recorded_at`: for the recording's [recorded at](https://musicbrainz.org/relationship/b06e6732-2603-47d3-8a49-9f589b430483) Event relationship
