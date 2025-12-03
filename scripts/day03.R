library(memoise)

lines <- readLines("assets/day03.txt")
inputs <- lapply(strsplit(lines, ""), as.integer)

.find_largest <- function(input, start_index, digits) {
  if (start_index > length(input)) {
    return(-Inf)
  }

  if (digits == 1) {
    max(input[start_index:length(input)])
  } else {
    max(
      sapply(
        start_index:length(input),
        function(s) (10**(digits - 1)) * input[s] + find_largest(input, s + 1, digits - 1)
      )
    )
  }
}
find_largest <- memoise(.find_largest)

ans1 <- sum(sapply(inputs, function(input) find_largest(input, 1, 2)))
cat("Part 1:", format(ans1, scientific = FALSE))

ans2 <- sum(sapply(inputs, function(input) find_largest(input, 1, 12)))
cat("Part 2:", format(ans2, scientific = FALSE))
