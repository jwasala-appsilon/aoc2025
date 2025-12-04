inputs <- readLines("assets/day04.txt")
inputs <- strsplit(inputs, "")
inputs <- sapply(inputs, function(s) strsplit(s, ""))

ans1 <- 0
ans2 <- 0
iter <- 0

while (TRUE) {
  to_remove <- c()

  for (i in seq_along(inputs[, 1])) {
    for (j in seq_along(inputs[i, ])) {
      if (inputs[i, j] == ".") {
        next
      }

      shifts <- c(-1, 0, 1)
      pairs <- split(as.matrix(expand.grid(shifts, shifts)), 1:9)

      counter <- 0

      for (pair in pairs) {
        if (pair[[1]] == 0 && pair[[2]] == 0) {
          next
        }

        if (i + pair[[1]] > length(inputs[, 1]) || i + pair[[1]] < 1 ||
              j + pair[[2]] > length(inputs[i, ]) || j + pair[[2]] < 1) {
          next
        }

        if (inputs[i + pair[[1]], j + pair[[2]]] == "@") {
          counter <- counter + 1
        }
      }

      if (counter < 4) {
        if (iter == 0) {
          ans1 <- ans1 + 1
        }
        ans2 <- ans2 + 1

        to_remove <- c(to_remove, list(list(i, j)))
      }
    }
  }

  for (point in to_remove) {
    inputs[point[[1]], point[[2]]] <- "."
  }

  iter <- iter + 1
  if (length(to_remove) == 0) {
    break
  }
}

cat("Part 1:", ans1)
cat("Part 2:", ans2)
