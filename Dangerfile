commit_message = git.commits.first.message
lines = commit_message.split("\n")

commit_title = lines.first
if commit_title.length > 50
  fail("❌ The commit title should not exceed 50 characters.")
end

if lines.length > 1 && !lines[1].strip.empty?
  fail("❌ There should be an empty line between the commit title and the description.")
end

commit_description = lines[2..-1]&.join("\n").to_s.strip
if commit_description.length > 0 && commit_description.length < 5
  fail("❌ The commit description must have at least 5 characters.")
end

commit_description.each_line do |line|
  if line.strip.length > 72
    fail("❌ Each line in the commit description should not exceed 72 characters.")
  end
end
