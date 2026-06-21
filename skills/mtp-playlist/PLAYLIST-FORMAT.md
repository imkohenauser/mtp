# mtp-playlist-{slug}.md Format

Use this format for MTP playlist artifacts and inline playlist output. The artifact should work both as a readable playlist document and as a copy-friendly source for playlist creation.

## Filename

When artifact or file output is available, create one Markdown file named `mtp-playlist-{slug}.md`.

Use lowercase kebab-case for `{slug}` based on the theme, artist, album, era, or source. If no stable slug can be formed, use `mtp-playlist-untitled.md`.

## Structure

- `Title`      : Short human-readable title in the form `MTP: {short title}`.
- `Prompt`     : The original user input that produced the playlist. Use a fenced `text` block for easy copying.
- `Metadata`   : Slug, curator, updated date, scope, pattern, track count, and genres.
- `Description`: One or two sentences describing the playlist's theme, source, and intended arc. Use a fenced `text` block for easy copying.
- `Tracklist`  : A copy-friendly plain-text list plus a rendered Markdown details table.
- `Notes`      : Optional. Include only when verification limits, uncertainty, sparse mapping, or unusual anchors need to be stated.

## Metadata labels

- `Slug`       : The `{slug}` used in the artifact filename.
- `Curator`    : The model or agent name. When useful and available, include the tool or host in parentheses.
- `Updated`    : Date in `YYYY-MM-DD` format.
- `Scope`      : `Full`, `Side A`, `Side B`, `Extended`, or `Source-limited`.
- `Pattern`    : MTP block pattern such as `1+9+9+1`, `1+9`, `9+1`, or the requested extended pattern.
- `Tracks`     : Number of rows actually output.
- `Genres`     : Main genres, scenes, or sound worlds. Use `Unknown` only when no stable label applies.

## Tracklist fields

- `Copy List`  : Plain-text list for copying into playlist tools. Format each row as `{number}. {Node}: {track} - {artist}`. For artist-themed playlists, use `{number}. {Node}: {track} ({source})`.
- `Details`    : Rendered Markdown table. Do not wrap this table in a code fence in the generated artifact.
- `#`          : MTP node number. Preserve original MTP node numbers for sparse source-limited mappings.
- `Node`       : MTP node name.
- `Track`      : Track, recording, composition, performance, sound work, or musical moment.
- `Artist`     : Artist, composer, performer, ensemble, or credited creator.
- `Source`     : Use instead of `Artist` for artist-themed playlists; describe album, version, feature, remix, sample origin, recording, or other source context.
- `Year`       : Recording or release year of the specific version. Leave blank when uncertain.
- `Reason`     : Listener-facing node-fit explanation grounded in audible evidence.

## Artifact template

The following block is fenced only because this file documents the template. In generated playlist artifacts, keep `Prompt`, `Description`, and `Copy List` fenced for copying, and keep the `Details` table unfenced so it renders as a table.

````markdown
# MTP: {short title}

## Prompt

```text
{user input}
```

## Metadata

- Slug        : {slug}
- Curator     : {model or agent name} ({tool or host, optional})
- Updated     : {YYYY-MM-DD}
- Scope       : {Full | Side A | Side B | Extended | Source-limited}
- Pattern     : {MTP block pattern}
- Tracks      : {number of output rows}
- Genres      : {genres, scenes, or sound worlds}

## Description

```text
{short description of the playlist}
```

## Tracklist

### Copy List

```text
1. Start: {track} - {artist}
```

### Details

| # | Node  | Track   | Artist   | Year   | Reason   |
|---|-------|---------|----------|--------|----------|
| 1 | Start | {track} | {artist} | {year} | {reason} |

## Notes

{optional note; omit this section when not needed}
````

## Artist-themed variant

For artist-themed playlists, use `Source` instead of `Artist` in `Details`, and use source context in `Copy List`.

```text
1. Start: {track} ({source})
```

```markdown
| # | Node  | Track   | Source   | Year   | Reason   |
|---|-------|---------|----------|--------|----------|
| 1 | Start | {track} | {source} | {year} | {reason} |
```

## Verification note

If external verification tools are unavailable, add this under `Notes`:

```markdown
Selections were restricted to tracks known with high confidence because external verification tools were unavailable.
```