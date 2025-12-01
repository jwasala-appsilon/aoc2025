lines <- readLines("assets/day01.txt")
dirs <- substring(lines, 1, 1)
steps <- as.integer(substring(lines, 2, 4))

pos <- 50
ans1 <- 0
ans2 <- 0

for (i in seq_along(dirs)) {
  dir <- dirs[i]
  step <- steps[i]
  prevpos <- pos

  if (dir == "L") {
    pos <- (pos - step)
  } else {
    pos <- (pos + step)
  }

  ans2 <- ans2 + abs((prevpos %/% 100) - (pos %/% 100))

  pos <- pos %% 100

  if (pos == 0) {
    ans1 <- ans1 + 1
  }


  if ((dir == "R" && pos == 0) ||
    (dir == "L" && prevpos == 0)) {
    ans2 <- ans2 - 1
  }
}

cat("Part 1:", ans1)

cat("Part 2:", ans2 + ans1)
