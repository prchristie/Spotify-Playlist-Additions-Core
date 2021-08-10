last_merged_branch=$(git log --merges -n 1)
branch_name="${last_merged_branch##*$'\n'}"

echo "Detected branch name '$branch_name'"

case "$branch_name" in
    *[MAJOR]*)
        echo "Detected MAJOR"; bump2version major;;
    *[MINOR]*)
        echo "Detected MINOR"; bump2version minor;;
    *[PATCH]*)
        echo "Detected PATCH"; bump2version patch;;
    *[IGNORE]*)
        echo "Ignoring"; exit;;
esac