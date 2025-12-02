input <- readLines("assets/day02.txt")
ranges <- strsplit(input, ",")[[1]]
ranges <- lapply(ranges, function(s) strsplit(s, "-")[[1]])

ans1 <- 0
ans2 <- 0

for (r in ranges) {
  start <- as.double(r[[1]])
  end <- as.double(r[[2]])

  for (i in start:end) {
    candidate <- as.character(i)
    len <- nchar(candidate)
    mid <- len / 2

    # Answer part 1
    if (len %% 2 == 0) {
      if (substr(candidate, 1, mid) == substr(candidate, mid + 1, len)) {
        ans1 <- ans1 + i
      }
    }

    # Answer part 2
    for (piece_len in 1:mid) {
      if (len %% piece_len != 0) {
        next
      }

      pieces <- len %/% piece_len

      if (pieces < 2) {
        next
      }

      first_piece <- substring(candidate, 1, piece_len)
      expected <- strrep(first_piece, pieces)

      if (candidate == expected) {
        ans2 <- ans2 + i
        break
      }
    }
  }
}

cat("Part 1:", ans1)
cat("Part 2:", ans2)
