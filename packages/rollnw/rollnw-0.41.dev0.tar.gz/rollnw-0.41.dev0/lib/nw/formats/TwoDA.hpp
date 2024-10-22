#pragma once

#include "../log.hpp"
#include "../resources/ResourceData.hpp"
#include "../util/string.hpp"

#include <span>

#include <filesystem>
#include <iostream>
#include <limits>
#include <optional>
#include <string>
#include <string_view>

namespace nw {

namespace detail {

// Not a variant, not for public consumption
struct StringVariant {
    StringVariant(const char* string)
        : str{string}
        , view{str}
    {
    }

    StringVariant(String string)
        : str{std::move(string)}
        , view{str}
    {
    }

    StringVariant(StringView string)
        : view{string}
    {
    }

    StringVariant(const StringVariant&) = delete;
    StringVariant(StringVariant&& other)
    {
        if (other.str.size()) {
            str = std::move(other.str);
            view = str;
        } else {
            view = other.view;
        }
    }
    StringVariant& operator=(const StringVariant&) = delete;
    StringVariant& operator=(StringVariant&& other)
    {
        if (this != &other) {
            if (other.str.size()) {
                str = std::move(other.str);
                view = str;
            } else {
                view = other.view;
            }
        }
        return *this;
    }

    String str;
    StringView view;
};

} // namespace detail

struct TwoDARowView;

// == TwoDA ===================================================================

struct TwoDA {
    static constexpr size_t npos = std::numeric_limits<size_t>::max();

    TwoDA() = default;
    TwoDA(const TwoDA&) = delete;
    TwoDA(TwoDA&&) = default;

    TwoDA& operator=(const TwoDA&) = delete;
    TwoDA& operator=(TwoDA&&) = default;

    /// Constructs TwoDA object from a file
    explicit TwoDA(const std::filesystem::path& filename);

    /// Constructs TwoDA object from an array of bytes
    explicit TwoDA(ResourceData data);

    /// Finds the index of a column, or -1
    size_t column_index(StringView column) const;

    /// Get the number of columns
    size_t columns() const noexcept;

    /// Gets an element
    template <typename T>
    std::optional<T> get(size_t row, size_t col) const;

    /// Gets an element
    template <typename T>
    std::optional<T> get(size_t row, StringView col) const;

    /// Gets an element
    template <typename T>
    bool get_to(size_t row, size_t col, T& out) const;

    /// Gets an element
    template <typename T>
    bool get_to(size_t row, StringView col, T& out) const;

    /// Pads the 2da with ``count`` rows.
    void pad(size_t count);

    /// Gets entire row as
    TwoDARowView row(size_t row) const noexcept;

    /// Number of rows
    size_t rows() const noexcept;

    /// Sets an element
    template <typename T>
    void set(size_t row, size_t col, const T& value);

    /// Sets an element
    template <typename T>
    void set(size_t row, StringView col, const T& value);

    /// Is the 2da parsed without error
    bool is_valid() const noexcept;

private:
    friend std::ostream& operator<<(std::ostream& out, const TwoDA& tda);

    ResourceData data_;
    bool is_loaded_ = false;

    String default_;
    Vector<size_t> widths_;
    Vector<String> columns_;
    Vector<detail::StringVariant> rows_;

    bool parse();
};

template <typename T>
std::optional<T> TwoDA::get(size_t row, size_t col) const
{
    T temp;
    return get_to(row, col, temp)
        ? std::optional<T>{std::move(temp)}
        : std::optional<T>{};
}

template <typename T>
std::optional<T> TwoDA::get(size_t row, StringView col) const
{
    size_t ci = column_index(col);
    if (ci == npos) {
        LOG_F(WARNING, "unknown column: {}", col);
        return std::optional<T>{};
    }

    return get<T>(row, ci);
}

template <typename T>
bool TwoDA::get_to(size_t row, size_t col, T& out) const
{
    static_assert(
        std::is_same_v<T, String> || std::is_same_v<T, float> || std::is_convertible_v<T, int32_t> || std::is_same_v<T, StringView>,
        "TwoDA only supports float, String, StringView, or anything convertible to int32_t");

    size_t idx = row * columns_.size() + col;
    CHECK_F(idx < rows_.size(), "Out of Bounds row {}, col {}", row, col);

    StringView res = rows_[idx].view;

    if (res == "****") return false;

    if constexpr (std::is_same_v<T, float> || std::is_convertible_v<T, int>) {
        auto opt = string::from<T>(res);
        if (!opt) return false;
        out = *opt;
    } else if constexpr (std::is_same_v<T, StringView>) {
        out = res;
    } else {
        out = String(res);
    }

    return true;
}

template <typename T>
bool TwoDA::get_to(size_t row, StringView col, T& out) const
{
    size_t ci = column_index(col);
    if (ci == npos) {
        LOG_F(WARNING, "unknown column: {}", col);
        return false;
    }
    return get_to<T>(row, ci, out);
}

template <typename T>
void TwoDA::set(size_t row, size_t col, const T& value)
{
    size_t idx = row * columns_.size() + col;
    if (idx >= rows_.size()) return;

    int quote = 0;
    if constexpr (std::is_floating_point_v<T> || std::is_integral_v<T>) {
        rows_[idx] = std::to_string(value);
    } else {
        rows_[idx] = value;
        if (rows_[idx].view.find(' ') != StringView::npos) {
            quote = 2;
        }
    }
    widths_[col] = std::max(widths_[col], rows_[idx].view.size() + quote);
}

template <typename T>
void TwoDA::set(size_t row, StringView col, const T& value)
{
    set<T>(row, column_index(col), value);
}

/// Overload for ``operator<<``
std::ostream& operator<<(std::ostream& out, const TwoDA& tda);

// == TwoDARowView ============================================================

/**
 * @brief A view of a row in a TwoDA file
 * @note This behaves as ``StringView``, i.e. constant view only
 */
struct TwoDARowView {
    std::span<const detail::StringVariant> data;
    const TwoDA* parent = nullptr;
    size_t row_number = TwoDA::npos;

    /// Gets an element
    template <typename T>
    std::optional<T> get(size_t col) const;

    /// Gets an element
    template <typename T>
    std::optional<T> get(StringView col) const;

    /// Gets an element
    template <typename T>
    bool get_to(size_t col, T& out) const;

    /// Gets an element
    template <typename T>
    bool get_to(StringView col, T& out) const;

    /// Gets the number of columns
    size_t size() const noexcept { return data.size(); }
};

template <typename T>
std::optional<T> TwoDARowView::get(size_t col) const
{
    if (!parent || col >= data.size()) {
        return {};
    }
    return parent->get<T>(row_number, col);
}

template <typename T>
std::optional<T> TwoDARowView::get(StringView col) const
{
    if (!parent) {
        return {};
    }
    return parent->get<T>(row_number, col);
}

template <typename T>
bool TwoDARowView::get_to(size_t col, T& out) const
{
    if (!parent || col >= data.size()) {
        return false;
    }
    return parent->get_to(row_number, col, out);
}

template <typename T>
bool TwoDARowView::get_to(StringView col, T& out) const
{
    if (!parent) {
        return false;
    }
    return parent->get_to(row_number, col, out);
}

} // namespace nw
