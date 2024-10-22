# Test Python Library

Library used to test a new simplified release flow.

## Development

A suggested method of development is to use git worktrees.

1. From a personal fork, create a new worktree for the bug, feature or chore.

git worktree add feature-a

2. Implement the code changes and commit.

3. Update the CHANGELOG.md to include the change in the "Unreleased" section.

4. Commit, push and create a PR to the upstream repository's main branch.

5. Solicit a code-read from another team member.

6. Upon approval, squash and merge to main.

7. (optional) cleanup by removing the worktree and associated local and remote
   branch.

If the version was incremented in pyproject.toml, the merge to the main branch
will trigger a release to test PyPI (but not production PyPI).

## Releasing
Only create a release for actual library updates.
Things that do not warrant a release:
- Repository metadata such as README updates, workflow
 changes, etc.
- Cleanup/refactors

1. Create a new branch "release-x.y.z"
   When incrementing, follow Semantic Versioning standard.
   - Bug fixes:  ++ patch version
   - Features:   ++ minor version
   - Breaking Changes:  ++ major version

2. Update pyproject.toml with the new version.

3. Update CHANGELOG.md by moving the "Unreleased" items into a new
   section for the given version (leaving an empty Unreleased section as a
   template for future updates)

4. Commit, push and create a PR to upstream's main branch
   Please set the commit message to "Release vx.y.z" with the new version number

5. Obtain approval for release from another team member.

6. Squash and merge (ensure the commit message remains Release vx.y.x).

7. Verify the new version was correctly published to test PyPI and all
   precautions have been taken to ensure it is functioning as intended.

8. Pull from upstream into your local main branch and tag the commit vx.y.z
   (the squash and merge will have created a new commit hash)

9. push the tag to upstream, triggering the release to production PyPI.




