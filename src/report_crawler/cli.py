import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="report-crawler")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("crawl", help="Thu thập bài viết")
    sub.add_parser("report", help="Tạo báo cáo từ dữ liệu đã thu thập")
    args = parser.parse_args()
    print(f"Lệnh: {args.command}")


if __name__ == "__main__":
    main()