inputs <- readLines("assets/day05.txt")

empty <- which(inputs == "")
ranges <- inputs[1:(empty - 1)]
indegrients <- inputs[(empty + 1):length(inputs)]

ranges <- lapply(strsplit(ranges, "-"), as.double)
indegrients <- lapply(indegrients, as.double)

# Part 1
ans1 <- 0

for (ingredient in ingredients) {
  for (range in ranges) {
    if (ingredient >= range[[1]] && ingredient <= range[[2]]) {
      ans1 <- ans1 + 1
      break
    }
  }
}

cat("Part 1", ans1)

# Part 2 in Python
